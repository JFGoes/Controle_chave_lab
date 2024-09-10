import flet as ft

def aluno_view(page, user_data):
    page.clean()

    def solicitar_chave(e):
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
                ft.Text(f"Bem-vindo, {user_data['nome']}!", size=20),
                ft.ElevatedButton("Solicitar Chave", on_click=solicitar_chave),
                ft.ElevatedButton("Devolver Chave", on_click=devolver_chave),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
