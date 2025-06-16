import sqlite3


def conectar():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            devolvido INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY(livro_id) REFERENCES livros(id),
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        );
    ''')

    # Verifica se já existe algum usuário cadastrado
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    count = cursor.fetchone()[0]
    if count == 0:
        # Insere um admin padrão
        cursor.execute(
            "INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)",
            ("admin", "admin123", "admin"))
        print("Admin padrão criado: usuário='admin', senha='admin123'")

    conn.commit()
    return conn
