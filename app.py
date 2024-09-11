import flet as ft
from database.db import criar_tabelas
from views.login_view import login_view
from views.aluno_view import aluno_view
from views.guarda_view import guarda_view
from views.professor_view import professor_view
from views.admin_view import admin_view
from controllers.autenticacao import login


def main(page: ft.Page):
    # Garantir que as tabelas sejam criadas no início
    criar_tabelas()

    # Função para realizar o login e redirecionar o usuário para a interface correta
    def realizar_login(usuario, senha, tipo_usuario):
        user_data = login(usuario, senha, tipo_usuario)
        if user_data is None:
            page.snack_bar = ft.SnackBar(ft.Text("Credenciais inválidas!"))
            page.snack_bar.open = True
            page.update()
        else:
            if tipo_usuario == 'Aluno':
                aluno_view(page, user_data)
            elif tipo_usuario == 'Guarda':
                guarda_view(page)
            elif tipo_usuario == 'Professor':
                professor_view(page)
            elif tipo_usuario == 'Admin':  # Verifica se é um administrador
                admin_view(page)

    # Carregar tela de login inicialmente
    login_view(page, realizar_login)


ft.app(target=main)
