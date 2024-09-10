# Simulação de um banco de dados simples
# Simulação de um banco de dados simples com matrículas
usuarios = {
    "admin": {"senha": "admin123", "tipo": "Admin", "nome": "Administrador", "id": 1},
    "aluno1": {
        "senha": "123",
        "tipo": "Aluno",
        "nome": "Aluno 1",
        "matricula": "2021001",  # Matrícula do aluno 1
        "com_chave": False,
        "id": 2
    },
    "guarda1": {
        "senha": "456",
        "tipo": "Guarda",
        "nome": "Guarda 1",
        "id": 3
    },
    "professor1": {
        "senha": "789",
        "tipo": "Professor",
        "nome": "Professor 1",
        "id": 4
    },
}

def login(usuario, senha, tipo_usuario):
    user = usuarios.get(usuario)
    if user and user["senha"] == senha and user["tipo"] == tipo_usuario:
        return user
    return None
