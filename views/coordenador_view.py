import flet as ft
from database.db import listar_alunos, inserir_usuario, deletar_usuario, listar_relatorio_diario


def coordenador_view(page):
    page.clean()

    # Função para carregar alunos
    def carregar_alunos():
        alunos = listar_alunos()  # Busca alunos no banco de dados
        return [ft.Text(f"{aluno['nome']} - Matrícula: {aluno['matricula']}") for aluno in alunos]

    # Função para cadastrar um novo aluno
    def cadastrar_aluno(e):
        inserir_usuario(
            nome_completo.value,
            nome_usuario.value,
            curso.value,
            matricula.value,
            rg.value,
            email.value,
            telefone.value,
            laboratorio_dropdown.value,
            tipo="Aluno",  # Coordenador só pode cadastrar alunos
            foto=foto.value
        )
        page.snack_bar = ft.SnackBar(
            ft.Text(f"{nome_completo.value} cadastrado com sucesso!"))
        page.snack_bar.open = True
        nome_completo.value = ""
        nome_usuario.value = ""
        curso.value = ""
        matricula.value = ""
        rg.value = ""
        email.value = ""
        telefone.value = ""
        page.update()

    # Função para deletar um aluno
    def deletar_aluno(e):
        # Deletar pelo número da matrícula
        deletar_usuario(matricula_deletar.value)
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Aluno com matrícula {matricula_deletar.value} deletado!"))
        page.snack_bar.open = True
        page.update()

    # Carregar o relatório diário
    def carregar_relatorio():
        relatorio = listar_relatorio_diario()
        return [ft.Text(f"Ação: {entry['acao']} - Aluno: {entry['aluno']} - Horário: {entry['timestamp']}") for entry in relatorio]

    # Interface de cadastro de alunos
    nome_completo = ft.TextField(label="Nome Completo")
    nome_usuario = ft.TextField(label="Nome de Usuário")
    curso = ft.TextField(label="Curso")
    matricula = ft.TextField(label="Matrícula")
    rg = ft.TextField(label="RG")
    email = ft.TextField(label="Email")
    telefone = ft.TextField(label="Telefone")
    laboratorio_dropdown = ft.Dropdown(label="Laboratório", options=[])
    foto = ft.FilePicker(allowed_extensions=[
                         "jpg", "jpeg", "png"], label="Carregar Foto")

    matricula_deletar = ft.TextField(label="Matrícula para Deletar")

    page.add(
        ft.Column(
            controls=[
                ft.Text("Painel do Coordenador", size=25, weight="bold"),

                # Seção de Cadastro de Alunos
                ft.Text("Cadastrar Alunos", size=20, weight="bold"),
                nome_completo, nome_usuario, curso, matricula, rg, email, telefone, laboratorio_dropdown, foto,
                ft.ElevatedButton("Cadastrar Aluno", on_click=cadastrar_aluno),

                # Seção de Deleção de Alunos
                ft.Text("Deletar Alunos", size=20, weight="bold"),
                matricula_deletar,
                ft.ElevatedButton("Deletar Aluno", on_click=deletar_aluno),

                # Exibir alunos cadastrados
                ft.Text("Alunos Cadastrados:", size=20),
                *carregar_alunos(),

                # Relatório diário de solicitações e devoluções
                ft.Text("Relatório Diário de Solicitações e Devoluções", size=20),
                *carregar_relatorio(),

                # Botão de sair para retornar ao login
                ft.ElevatedButton("Sair", on_click=lambda _: login_view(page))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
