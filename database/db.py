import sqlite3

# Função para conectar ao banco de dados


def conectar():
    return sqlite3.connect("controle_chaves.db")

# Função para criar as tabelas ou modificar as existentes


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de usuários (sem relacionamento com laboratórios)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nome_usuario TEXT UNIQUE NOT NULL,
        curso TEXT,
        matricula TEXT UNIQUE,
        rg TEXT,
        email TEXT,
        telefone TEXT,
        laboratorio TEXT,  -- Laboratório agora é um campo de texto
        tipo TEXT NOT NULL,  -- Aluno, Professor, Guarda, Admin
        foto TEXT
    )
    ''')

    # Tabela de solicitações de chaves
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS solicitacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        solicitacao_status TEXT DEFAULT 'pendente',
        data_solicitacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
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
    # Verificar se o admin já existe
    cursor.execute('''
    SELECT * FROM usuarios WHERE nome_usuario = 'admin'
    ''')
    admin_exists = cursor.fetchone()

    # Se o admin não existir, vamos criá-lo com a senha padrão
    if not admin_exists:
        cursor.execute('''
        INSERT INTO usuarios (nome, nome_usuario, tipo, curso, matricula, rg, email, telefone)
        VALUES ('Administrador', 'admin', 'Admin', NULL, NULL, NULL, NULL, NULL)
        ''')

    # Removemos a tabela de laboratórios
    conn.commit()
    conn.close()

# Função para inserir um novo usuário no banco de dados


def inserir_usuario(nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, foto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO usuarios (nome, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, foto)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, foto))

    conn.commit()
    conn.close()


# Função para buscar um usuário pelo login (nome de usuário)
def buscar_usuario_por_login(nome_usuario):
    conn = conectar()
    cursor = conn.cursor()

    # Seleciona os campos do usuário, incluindo o laboratório (agora um campo de texto)
    cursor.execute('''
    SELECT id, nome, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, foto
    FROM usuarios
    WHERE nome_usuario = ?
    ''', (nome_usuario,))

    usuario = cursor.fetchone()
    conn.close()

    # Retorna os dados do usuário, incluindo o laboratório
    return usuario


def buscar_solicitacoes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT s.id, u.nome AS nome_usuario, s.solicitacao_status, s.data_solicitacao
    FROM solicitacoes s
    JOIN usuarios u ON u.id = s.usuario_id
    WHERE s.solicitacao_status = 'pendente'
    ''')

    solicitacoes = cursor.fetchall()
    conn.close()

    return [{"id": row[0], "nome_usuario": row[1], "status": row[2], "data_solicitacao": row[3]} for row in solicitacoes]

# Função para atualizar o status de uma solicitação


def atualizar_solicitacao(solicitacao_id, novo_status):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE solicitacoes
    SET solicitacao_status = ?
    WHERE id = ?
    ''', (novo_status, solicitacao_id))

    conn.commit()
    conn.close()

# Função para criar laboratórios


def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT nome, matricula
    FROM usuarios
    WHERE tipo = 'Aluno'
    ''')

    alunos = cursor.fetchall()
    conn.close()

    return [{"nome": row[0], "matricula": row[1]} for row in alunos]


def deletar_usuario(matricula):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM usuarios
    WHERE matricula = ?
    ''', (matricula,))

    conn.commit()
    conn.close()


def listar_relatorio_diario():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT u.nome AS aluno, h.acao, h.timestamp
    FROM historico h
    JOIN usuarios u ON u.id = h.aluno_id
    WHERE DATE(h.timestamp) = DATE('now')
    ORDER BY h.timestamp DESC
    ''')

    relatorio = cursor.fetchall()
    conn.close()

    return [{"aluno": row[0], "acao": row[1], "timestamp": row[2]} for row in relatorio]


def listar_historico():
    conn = conectar()
    cursor = conn.cursor()

    # Executa a consulta para listar as ações do histórico
    cursor.execute('''
    SELECT u.nome AS aluno, h.acao, h.timestamp
    FROM historico h
    JOIN usuarios u ON u.id = h.aluno_id
    ORDER BY h.timestamp DESC
    ''')

    historico = cursor.fetchall()
    conn.close()

    # Retorna uma lista de dicionários com as informações do histórico
    return [{"aluno": row[0], "acao": row[1], "timestamp": row[2]} for row in historico]
