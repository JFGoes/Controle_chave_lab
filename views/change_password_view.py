import flet as ft
from database.db import atualizar_senha
from views.login_view import login_view


def change_password_view(page, usuario_id, realizar_login):
    page.clean()

    # Campos para nova senha e confirmação
    nova_senha = ft.TextField(
        label="Nova Senha", password=True, can_reveal_password=True)
    confirmar_senha = ft.TextField(
        label="Confirmar Nova Senha", password=True, can_reveal_password=True)

    # Função para processar a alteração de senha
    def alterar_senha(e):
        if nova_senha.value != confirmar_senha.value:
            page.snack_bar = ft.SnackBar(ft.Text("As senhas não coincidem!"))
            page.snack_bar.open = True
            page.update()
            return

        # Atualiza a senha no banco de dados
        atualizar_senha(usuario_id, nova_senha.value)
        page.snack_bar = ft.SnackBar(ft.Text("Senha alterada com sucesso!"))
        page.snack_bar.open = True
        page.update()

    # Adiciona os controles à página
    page.add(
        ft.Column(
            controls=[
                ft.Text("Alterar Senha", size=30, weight="bold"),
                nova_senha,
                confirmar_senha,
                ft.ElevatedButton("Alterar Senha", on_click=alterar_senha),
                ft.ElevatedButton("Sair", on_click=lambda _: login_view(
                    page, realizar_login))  # Botão de sair
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
