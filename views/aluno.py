import flet as ft
from controllers.chave_controller import solicitar_chave, devolver_chave

def aluno_view(page, user_data):
    page.clean()
    
    # Verificar se o aluno está com a chave
    if user_data["com_chave"]:
        devolver_button = ft.ElevatedButton("Devolver Chave", on_click=lambda e: devolver_chave(user_data["id"], page))
    else:
        devolver_button = ft.ElevatedButton("Solicitar Chave", on_click=lambda e: solicitar_chave(user_data["id"], page))

    page.add(
        ft.Column(
            controls=[
                ft.Text(f"Bem-vindo {user_data['nome']}!", size=20),
                devolver_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
