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
        senha TEXT,  -- Adicionando o campo para armazenar a senha
        foto TEXT
    )
    ''')

    # Tabela de solicitações de chaves
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS solicitacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        chave_id INTEGER,
        status TEXT DEFAULT 'Solicitado',
        data_solicitacao DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (aluno_id) REFERENCES usuarios(id)
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

    # Se o Admin não existir, criar com a senha padrão 'admin123'
    if not admin_exists:
        cursor.execute('''
        INSERT INTO usuarios (nome, nome_usuario, tipo, senha)
        VALUES ('Administrador', 'admin', 'Admin', 'admin123')
        ''')

    # Removemos a tabela de laboratórios
    conn.commit()
    conn.close()


def registrar_solicitacao_chave(aluno_id, chave_id):
    conn = conectar()
    cursor = conn.cursor()

    # Inserir a solicitação no banco de dados
    cursor.execute('''
    INSERT INTO solicitacoes (aluno_id, chave_id, status)
    VALUES (?, ?, 'Solicitado')
    ''', (aluno_id, chave_id))

    conn.commit()
    conn.close()


# Função para buscar um usuário pelo login (nome de usuário)
def buscar_usuario_por_login(nome_usuario):
    conn = conectar()
    cursor = conn.cursor()

    # Seleciona os campos do usuário, incluindo o laboratório (agora um campo de texto)
    cursor.execute('''
    SELECT id, nome, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, senha, foto
    FROM usuarios
    WHERE nome_usuario = ?
    ''', (nome_usuario,))

    usuario = cursor.fetchone()
    conn.close()

    # Retorna os dados do usuário, incluindo o laboratório
    return usuario

# Função para inserir um novo usuário no banco de dados


def inserir_usuario(nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, senha, foto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO usuarios (nome, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo,senha, foto)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    ''', (nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, senha, foto))

    conn.commit()
    conn.close()


def atualizar_senha(usuario_id, nova_senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE usuarios
    SET senha = ?
    WHERE id = ?
    ''', (nova_senha, usuario_id))

    conn.commit()
    conn.close()


def buscar_solicitacoes_pendentes():
    conn = conectar()
    cursor = conn.cursor()

    # Buscar todas as solicitações que ainda estão com status "Solicitado"
    cursor.execute('''
    SELECT s.id, u.nome, s.chave_id, s.data_solicitacao
    FROM solicitacoes s
    JOIN usuarios u ON s.aluno_id = u.id
    WHERE s.status = 'Solicitado'
    ''')

    solicitacoes = cursor.fetchall()
    conn.close()

    return solicitacoes

# Função para atualizar o status de uma solicitação


def atualizar_status_solicitacao(solicitacao_id, novo_status):
    conn = conectar()
    cursor = conn.cursor()

    # Atualizar o status da solicitação (Autorizado, Negado)
    cursor.execute('''
    UPDATE solicitacoes
    SET status = ?
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


def listar_historico_chaves():
    conn = conectar()
    cursor = conn.cursor()

    # Consultar todas as solicitações de chaves, juntando com as informações dos alunos e do status
    cursor.execute('''
    SELECT s.id, u.nome, s.chave_id, s.status, s.data_solicitacao
    FROM solicitacoes s
    JOIN usuarios u ON s.aluno_id = u.id
    ORDER BY s.data_solicitacao DESC
    ''')

    historico = cursor.fetchall()
    conn.close()

    return historico

# def listar_historico():
#     conn = conectar()
#     cursor = conn.cursor()

#     # Executa a consulta para listar as ações do histórico
#     cursor.execute('''
#     SELECT u.nome AS aluno, h.acao, h.timestamp
#     FROM historico h
#     JOIN usuarios u ON u.id = h.aluno_id
#     ORDER BY h.timestamp DESC
#     ''')

#     historico = cursor.fetchall()
#     conn.close()

#     # Retorna uma lista de dicionários com as informações do histórico
#     return [{"aluno": row[0], "acao": row[1], "timestamp": row[2]} for row in historico]
