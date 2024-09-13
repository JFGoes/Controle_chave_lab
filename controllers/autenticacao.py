from database.db import buscar_usuario_por_login


def login(nome_usuario, senha, tipo_usuario):
    usuario = buscar_usuario_por_login(nome_usuario)

    if usuario is None:
        return None  # Usuário não encontrado

    # Descompactar os dados retornados do banco de dados
    usuario_id, nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio, tipo, senha_bd, foto = usuario

    # Verifica se a senha corresponde
    if senha != senha_bd:
        return None  # Senha incorreta

    # Verifica se o tipo de usuário corresponde ao tipo esperado (Aluno, Professor, Guarda, etc.)
    if tipo != tipo_usuario:
        return None  # Senha

    return {
        "id": usuario_id,
        "nome_completo": nome_completo,
        "nome_usuario": nome_usuario,
        "curso": curso,
        "matricula": matricula,
        "rg": rg,
        "email": email,
        "telefone": telefone,
        "laboratorio": laboratorio,  # O campo de laboratório retornado
        "tipo": tipo,
        "foto": foto
    }
