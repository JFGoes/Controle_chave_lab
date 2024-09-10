import flet as ft
from database.db import inserir_laboratorio, inserir_usuario, listar_laboratorios

def admin_view(page):

    # Campos para cadastrar laboratório
    laboratorio_nome = ft.TextField(label="Nome do Laboratório", autofocus=True)

    def cadastrar_laboratorio(e):
        inserir_laboratorio(laboratorio_nome.value)
        page.snack_bar = ft.SnackBar(ft.Text(f"Laboratório {laboratorio_nome.value} cadastrado com sucesso!"))
        page.snack_bar.open = True
        laboratorio_nome.value = ""  # Limpa o campo após o cadastro
        page.update()

    # Campos para cadastrar usuários (alunos, professores, guardas)
    nome_usuario = ft.TextField(label="Nome do Usuário")
    matricula_usuario = ft.TextField(label="Matrícula do Usuário")
    senha_usuario = ft.TextField(label="Senha do Usuário", password=True, can_reveal_password=True)
    tipo_usuario = ft.Dropdown(
        label="Tipo de Usuário",
        options=[
            ft.dropdown.Option("Aluno"),
            ft.dropdown.Option("Professor"),
            ft.dropdown.Option("Guarda")
        ]
    )

    laboratorio_dropdown = ft.Dropdown(
        label="Laboratório",
        options=[
            ft.dropdown.Option(str(lab[0]), lab[1]) for lab in listar_laboratorios()
        ]
    )

    def cadastrar_usuario(e):
        inserir_usuario(
            nome_usuario.value,
            matricula_usuario.value,
            senha_usuario.value,
            tipo_usuario.value,
            laboratorio_id=laboratorio_dropdown.value
        )
        page.snack_bar = ft.SnackBar(ft.Text(f"Usuário {nome_usuario.value} cadastrado com sucesso!"))
        page.snack_bar.open = True
        nome_usuario.value = ""
        matricula_usuario.value = ""
        senha_usuario.value = ""
        tipo_usuario.value = ""
        laboratorio_dropdown.value = ""
        page.update()

    # Exibição da tela do admin
    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Painel do Administrador", size=30, weight="bold"),
                
                ft.Divider(height=10),
                ft.Text("Cadastrar Laboratório"),
                laboratorio_nome,
                ft.ElevatedButton("Cadastrar Laboratório", on_click=cadastrar_laboratorio),

                ft.Divider(height=30),
                ft.Text("Cadastrar Usuários"),
                nome_usuario,
                matricula_usuario,
                senha_usuario,
                tipo_usuario,
                laboratorio_dropdown,
                ft.ElevatedButton("Cadastrar Usuário", on_click=cadastrar_usuario),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
