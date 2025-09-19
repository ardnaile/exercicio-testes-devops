import sqlite3

def conectarbanco():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT)')
    return conn, cursor

def cadastrarusuario(nome):
    conn, cursor = conectarbanco()
    if nome is None:
        raise ValueError("Nome inválido")
    cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
    conn.commit()
    cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome,))
    return cursor.fetchone()
