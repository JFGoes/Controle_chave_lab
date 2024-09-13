import flet as ft
from database.db import registrar_solicitacao_chave


def aluno_view(page, aluno_data):
    aluno_id = aluno_data["id"]  # Pegar o ID do aluno do dado passado
    # ID da chave que o aluno deseja solicitar
    chave_id = ft.TextField(label="ID da Chave")

    def solicitar_chave(e):
        registrar_solicitacao_chave(aluno_id, chave_id.value)
        page.snack_bar = ft.SnackBar(ft.Text("Chave solicitada com sucesso!"))
        page.snack_bar.open = True
        page.update()

    def devolver_chave(e):
        page.snack_bar = ft.SnackBar(ft.Text("Chave devolvida com sucesso!"))
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(f"Bem-vindo, {aluno_data['nome_usuario']}!", size=20),
                ft.ElevatedButton("Solicitar Chave", on_click=solicitar_chave),
                ft.ElevatedButton("Devolver Chave", on_click=devolver_chave),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
