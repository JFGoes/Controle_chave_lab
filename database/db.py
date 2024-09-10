import sqlite3

# Função para conectar ao banco de dados


def conectar():
    return sqlite3.connect("controle_chaves.db")

# Função para criar as tabelas se elas ainda não existirem


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL,  -- Aluno, Professor, Guarda, Admin
        com_chave BOOLEAN NOT NULL DEFAULT 0,
        laboratorio_id INTEGER,
        FOREIGN KEY (laboratorio_id) REFERENCES laboratorios(id)
    )
    ''')

    # Tabela de laboratórios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS laboratorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )
    ''')

    # Tabela de histórico de retirada e devolução de chaves
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        acao TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (aluno_id) REFERENCES usuarios(id)
    )
    ''')

    conn.commit()
    conn.close()


def inserir_laboratorio(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO laboratorios (nome)
    VALUES (?)
    ''', (nome,))

    conn.commit()
    conn.close()


def inserir_usuario(nome, matricula, senha, tipo, laboratorio_id=None):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO usuarios (nome, matricula, senha, tipo, laboratorio_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, matricula, senha, tipo, laboratorio_id))

    conn.commit()
    conn.close()


def listar_laboratorios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT id, nome FROM laboratorios')
    laboratorios = cursor.fetchall()

    conn.close()
    return laboratorios


def buscar_usuario_por_matricula(matricula, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, nome, matricula, tipo, com_chave
    FROM usuarios
    WHERE matricula = ? AND senha = ?
    ''', (matricula, senha))

    usuario = cursor.fetchone()
    conn.close()

    return usuario


def registrar_acao(aluno_id, acao):
    conn = conectar()
    cursor = conn.cursor()

    # Inserir no histórico
    cursor.execute('''
    INSERT INTO historico (aluno_id, acao)
    VALUES (?, ?)
    ''', (aluno_id, acao))

    # Atualizar o status do aluno (se ele pegou ou devolveu a chave)
    if acao == 'retirada':
        cursor.execute(
            'UPDATE usuarios SET com_chave = 1 WHERE id = ?', (aluno_id,))
    elif acao == 'devolucao':
        cursor.execute(
            'UPDATE usuarios SET com_chave = 0 WHERE id = ?', (aluno_id,))

    conn.commit()
    conn.close()


def listar_historico():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT u.nome AS aluno, h.acao, h.timestamp
    FROM historico h
    JOIN usuarios u ON u.id = h.aluno_id
    ORDER BY h.timestamp DESC
    ''')

    historico = cursor.fetchall()
    conn.close()

    # Adicionar um print para verificar se o histórico está retornando dados
    print(historico)

    return [{"aluno": row[0], "acao": row[1], "timestamp": row[2]} for row in historico]
