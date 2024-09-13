import flet as ft

def login_view(page, realizar_login):
    nome_usuario = ft.TextField(label="Nome de Usuário", autofocus=True)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    tipo_usuario = ft.Dropdown(
        label="Tipo de Usuário",
        options=[
            ft.dropdown.Option("Aluno"),
            ft.dropdown.Option("Professor"),
            ft.dropdown.Option("Guarda"),
            ft.dropdown.Option("Coordenador"),
            ft.dropdown.Option("Admin")
        ]
    )

    def login_clicked(e):
        # Verificação se todos os campos estão preenchidos
        if not nome_usuario.value or not senha.value or not tipo_usuario.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
            return
        
        realizar_login(nome_usuario.value, senha.value, tipo_usuario.value)

    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Login KeyLab", size=30, weight="bold"),
                nome_usuario,
                senha,
                tipo_usuario,
                ft.ElevatedButton("Entrar", on_click=login_clicked),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
