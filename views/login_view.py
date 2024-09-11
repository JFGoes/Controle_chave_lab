import flet as ft

def login_view(page, realizar_login):
    matricula_input = ft.TextField(label="Matrícula", autofocus=True)
    senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    tipo_usuario = ft.Dropdown(
        label="Tipo de Usuário",
        options=[
            ft.dropdown.Option("Aluno"),
            ft.dropdown.Option("Professor"),
            ft.dropdown.Option("Guarda"),
            ft.dropdown.Option("Admin")
        ],
    )

    def login_clicked(e):
        realizar_login(matricula_input.value, senha_input.value, tipo_usuario.value)

    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Login KeyLab", size=30, weight="bold"),
                matricula_input,
                senha_input,
                tipo_usuario,
                ft.ElevatedButton("Entrar", on_click=login_clicked),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
