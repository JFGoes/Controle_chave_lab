from database.db import buscar_usuario_por_matricula

def login(matricula, senha, tipo_usuario):
    usuario = buscar_usuario_por_matricula(matricula, senha)
    
    if usuario is None:
        return None  # Nenhum usuário encontrado
    
    # Desempacotar os dados do usuário retornado
    usuario_id, nome, matricula, tipo, com_chave = usuario

    # Verificar se o tipo de usuário corresponde (Aluno, Professor, Guarda, Admin)
    if tipo == tipo_usuario:
        return {
            "id": usuario_id,
            "nome": nome,
            "matricula": matricula,
            "tipo": tipo,
            "com_chave": com_chave
        }
    
    return None  # Retorna None se o tipo de usuário não corresponder
