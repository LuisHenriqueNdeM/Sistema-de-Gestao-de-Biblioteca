# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto é um **sistema de gerenciamento de biblioteca** simples, desenvolvido em **Python**, com **interface gráfica (Tkinter)** e persistência de dados via **banco de dados SQLite**. Ele permite o controle de usuários, livros e empréstimos, com autenticação de **alunos** e **administradores**.

---

## ✨ Funcionalidades

### 🔐 Login com autenticação
- Login com **nome de usuário** e **senha**.
- Dois perfis de usuário:
  - **Administrador**:
    - Cadastrar livros e usuários (aluno ou admin)
    - Listar livros
    - Realizar empréstimos
    - Listar todos os empréstimos
  - **Aluno**:
    - Pode se cadastrar no sistema
    - Listar livros disponíveis
    - Visualizar seus empréstimos
    - Devolver livros

### 💾 Banco de dados (SQLite)
- O sistema usa `sqlite3` para armazenar todos os dados:
  - Tabela `usuarios`
  - Tabela `livros`
  - Tabela `emprestimos`

---

## 🧱 Estrutura do Projeto

```
biblioteca/
├── banco.py                  # Gerencia criação e conexão com o banco de dados
├── modelos/                  # (Opcional) Representação de entidades com dataclasses
│   ├── usuario.py
│   ├── livro.py
│   └── emprestimo.py
├── servicos/
│   └── biblioteca_service.py # Contém a lógica de negócio (funções para manipular dados)
main.py                       # Interface gráfica principal (Tkinter)
README.md                     # Documentação do projeto
```

---

## ⚙️ Como executar o projeto

### ✅ Requisitos
- Python 3.10 ou superior
- Módulos padrões: `tkinter`, `sqlite3`, `os`, `datetime`

> Nenhuma instalação de dependências externas é necessária.

### ▶️ Passos para execução
1. Faça o download/clonagem do projeto.
2. Abra o terminal (cmd, PowerShell, terminal Linux, etc.)
3. Acesse a pasta onde está o arquivo `main.py`.
4. Execute o projeto com o comando:
```bash
python main.py
```

### 📦 Primeira execução
- O banco de dados será criado automaticamente na primeira execução (`biblioteca.db`).
- Nenhum administrador existe por padrão. Cadastre um **novo administrador** clicando em "Cadastrar Usuário" e escolhendo o tipo `admin`.

---

## 📸 Interface Gráfica

A interface gráfica foi feita com o **Tkinter**, e inclui:
- Tela de login
- Tela de cadastro
- Menus separados para alunos e administradores
- Formulários para cadastro, devolução e empréstimo

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia  | Finalidade                      |
|-------------|---------------------------------|
| Python 3    | Lógica e estrutura do sistema   |
| SQLite      | Armazenamento de dados          |
| Tkinter     | Interface gráfica (GUI)         |
| OS / Datetime | Utilidades de sistema e datas  |

---

## 🔐 Regras de Acesso

| Tipo de Usuário | Ações Permitidas                           |
|-----------------|--------------------------------------------|
| `admin`         | Cadastrar livros e usuários, emprestar e listar tudo |
| `aluno`         | Cadastrar a si mesmo, listar livros, devolver livro |

---

## 🔄 Futuras Melhorias (sugestões)

- Validação de campos (evitar duplicidade ou dados vazios)
- Criptografia de senhas
- Pesquisa de livros por título
- Exportação de relatórios (PDF, Excel)
- Interface gráfica com bibliotecas modernas (ex: `customtkinter`)

---

## 👨‍💻 Autor

- **Luís Henrique** – Desenvolvedor do sistema  
- Assistência: **ChatGPT (OpenAI)** como tutor virtual

---

## 🧾 Licença

Este projeto é de uso educacional e livre para estudo, aprimoramento e adaptação.

---

## 📬 Contato

Caso deseje compartilhar sugestões ou tirar dúvidas:

📧 Email: [luishenrique.ndm@email.com]  
📘 GitHub: [github.com/LuisHenriqueNdeM]
