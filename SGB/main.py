import tkinter as tk
from tkinter import messagebox, simpledialog
import servicos.biblioteca_service as svc


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.usuario = None
        self.tela_login()

    def tela_login(self):
        for w in self.root.winfo_children():
            w.destroy()
        tk.Label(self.root, text="Nome:").pack(pady=5)
        self.e_nome = tk.Entry(self.root)
        self.e_nome.pack()
        tk.Label(self.root, text="Senha:").pack(pady=5)
        self.e_senha = tk.Entry(self.root, show="*")
        self.e_senha.pack()
        tk.Button(self.root, text="Login", command=self.logar).pack(pady=10)

    def logar(self):
        nome = self.e_nome.get()
        senha = self.e_senha.get()
        row = svc.autenticar_usuario(nome, senha)
        if not row:
            messagebox.showerror("Erro", "Login inválido")
        else:
            self.usuario = {"id": row[0], "nome": row[1], "tipo": row[2]}
            self.tela_principal()

    def tela_principal(self):
        for w in self.root.winfo_children():
            w.destroy()
        tk.Label(
            self.root, text=f"Bem-vindo(a), {self.usuario['nome']}").pack(pady=5)
        if self.usuario["tipo"] == "admin":
            tk.Button(self.root, text="Cadastrar Livro",
                      command=self.cadastrar_livro).pack(fill='x')
            tk.Button(self.root, text="Cadastrar Usuário",
                      command=self.cadastrar_usuario).pack(fill='x')
            tk.Button(self.root, text="Listar Livros",
                      command=self.listar_livros_admin).pack(fill='x')
            tk.Button(self.root, text="Fazer Empréstimo",
                      command=self.realizar_emprestimo).pack(fill='x')
            tk.Button(self.root, text="Listar Empréstimos",
                      command=self.listar_emprestimos_admin).pack(fill='x')
        else:
            tk.Button(self.root, text="Listar Livros",
                      command=self.listar_livros_admin).pack(fill='x')
            tk.Button(self.root, text="Meus Empréstimos",
                      command=self.listar_meus_emprestimos).pack(fill='x')
            tk.Button(self.root, text="Devolver Livro",
                      command=self.devolver_meu).pack(fill='x')
        tk.Button(self.root, text="Sair", command=self.tela_login).pack(
            fill='x', pady=10)

    def cadastrar_livro(self):
        titulo = simpledialog.askstring("Livro", "Título:")
        autor = simpledialog.askstring("Livro", "Autor:")
        ano = simpledialog.askinteger("Livro", "Ano:")
        if titulo and autor and ano:
            svc.cadastrar_livro(titulo, autor, ano)
            messagebox.showinfo("Sucesso", "Livro cadastrado")

    def cadastrar_usuario(self):
        nome = simpledialog.askstring("Usuário", "Nome:")
        senha = simpledialog.askstring("Usuário", "Senha:", show='*')
        tipo = simpledialog.askstring("Usuário", "Tipo (admin/aluno):")
        if nome and senha and tipo in ("admin", "aluno"):
            svc.cadastrar_usuario(nome, senha, tipo)
            messagebox.showinfo("Sucesso", "Usuário cadastrado")
        else:
            messagebox.showerror("Erro", "Dados inválidos")

    def listar_livros_admin(self):
        rows = svc.listar_livros()
        texto = "\n".join([f"{r[0]} - {r[1]} ({r[2]}, {r[3]})" for r in rows])
        messagebox.showinfo("Livros", texto or "Nenhum livro cadastrado")

    def realizar_emprestimo(self):
        livro_id = simpledialog.askinteger("Empréstimo", "ID do livro:")
        if livro_id:
            ok = svc.realizar_emprestimo(livro_id, self.usuario['id'])
            messagebox.showinfo(
                "Resultado", "Empréstimo OK" if ok else "Falha no empréstimo")

    def listar_emprestimos_admin(self):
        rows = svc.listar_emprestimos()
        texto = "\n".join(
            [f"{r[0]} - {r[1]} (Usuário: {r[2]}) - {'Devolvido' if r[3] else 'Em aberto'}" for r in rows])
        messagebox.showinfo("Empréstimos", texto or "Sem empréstimos")

    def listar_meus_emprestimos(self):
        rows = svc.listar_emprestimos(
            todos=False, usuario_id=self.usuario['id'])
        texto = "\n".join(
            [f"{r[0]} - {r[1]} - {'Devolvido' if r[3] else 'Em aberto'}" for r in rows])
        messagebox.showinfo("Meus empréstimos",
                            texto or "Você não possui empréstimos")

    def devolver_meu(self):
        emp_id = simpledialog.askinteger("Devolver", "ID do seu empréstimo:")
        if emp_id and svc.devolver_emprestimo(emp_id):
            messagebox.showinfo("OK", "Devolução realizada")
        else:
            messagebox.showerror("Erro", "Falha na devolução")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
