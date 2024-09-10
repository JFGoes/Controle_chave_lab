import flet as ft


def login_view(page, realizar_login):
    usuario = ft.TextField(label="Usuário", autofocus=True)
    senha = ft.TextField(label="Senha", password=True,
                         can_reveal_password=True)
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
        realizar_login(usuario.value, senha.value, tipo_usuario.value)

    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Login KeyLab", size=30, weight="bold"),
                usuario,
                senha,
                tipo_usuario,
                ft.ElevatedButton("Entrar", on_click=login_clicked),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
