import flet as ft
from database.db import criar_tabelas
from views.login_view import login_view
from views.admin_view import admin_view
from views.aluno_view import aluno_view
from views.guarda_view import guarda_view
from views.coordenador_view import coordenador_view
from views.professor_view import professor_view
from controllers.autenticacao import login


def main(page: ft.Page):
   # page.bgcolor = "green"
    page.window_width = 480
    page.window_height = 800
    page.padding = 10
    page.padding = 10
    page.scroll = "adaptive"  # Permitindo rolagem conforme necessário
    # Garantir que as tabelas sejam criadas no início
    criar_tabelas()
    # Função para realizar o login e redirecionar o usuário para a interface correta

    def realizar_login(nome_usuario, senha, tipo_usuario):
        user_data = login(nome_usuario, senha, tipo_usuario)
        if user_data is None:
            page.snack_bar = ft.SnackBar(ft.Text("Credenciais inválidas!"))
            page.snack_bar.open = True
            page.update()
        else:
            if tipo_usuario == 'Aluno':
                aluno_view(page, user_data)
            elif tipo_usuario == 'Guarda':
                guarda_view(page)
            elif tipo_usuario == 'Coordenador':
                coordenador_view(page)
            elif tipo_usuario == 'Professor':
                professor_view(page)
            elif tipo_usuario == 'Admin':
                admin_view(page, realizar_login)
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Acesso não permitido!"))
                page.snack_bar.open = True
                page.update()

    # Carregar a tela de login inicialmente
    login_view(page, realizar_login)


ft.app(target=main)
