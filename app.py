import flet as ft
from database.db import criar_tabelas
from views.login import login_view
from views.aluno import aluno_view
from views.guarda import guarda_view
from views.professor import professor_view
from controllers.autenticacao import login


def main(page: ft.Page):
    page.title = "Controle de Chave do Laboratório"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    criar_tabelas()  # Criar tabelas no banco de dados
    # Definir uma função de login para autenticar usuários

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

    # Inicialmente, carregamos a tela de login
    login_view(page, realizar_login)


ft.app(target=main)
