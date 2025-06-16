from banco import conectar

def cadastrar_usuario(nome, senha, tipo="aluno"):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)",
        (nome, senha, tipo)
    )
    conn.commit()
    conn.close()

def autenticar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, tipo FROM usuarios WHERE nome=? AND senha=?",
        (nome, senha)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def cadastrar_livro(titulo, autor, ano):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo, autor, ano)
    )
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, ano FROM livros")
    rows = cursor.fetchall()
    conn.close()
    return rows

def realizar_emprestimo(livro_id, usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM emprestimos WHERE livro_id=? AND devolvido=0",
        (livro_id,)
    )
    if cursor.fetchone()[0] > 0:
        conn.close()
        return False
    cursor.execute(
        "INSERT INTO emprestimos (livro_id, usuario_id) VALUES (?, ?)",
        (livro_id, usuario_id)
    )
    conn.commit()
    conn.close()
    return True

def listar_emprestimos(todos=True, usuario_id=None):
    conn = conectar()
    cursor = conn.cursor()
    if todos:
        cursor.execute("""
            SELECT e.id, l.titulo, u.nome, e.devolvido
            FROM emprestimos e
            JOIN livros l ON l.id=e.livro_id
            JOIN usuarios u ON u.id=e.usuario_id
        """)
    else:
        cursor.execute("""
            SELECT e.id, l.titulo, u.nome, e.devolvido
            FROM emprestimos e
            JOIN livros l ON l.id=e.livro_id
            JOIN usuarios u ON u.id=e.usuario_id
            WHERE e.usuario_id=?
        """, (usuario_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def devolver_emprestimo(emprestimo_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE emprestimos SET devolvido=1 WHERE id=?",
        (emprestimo_id,)
    )
    conn.commit()
    sucesso = cursor.rowcount > 0
    conn.close()
    return sucesso

