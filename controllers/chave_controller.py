import flet as ft
from controllers.dados import notificacoes_professor, historico_chaves
from controllers.autenticacao import usuarios  # Importe o dicionário 'usuarios'
from views.professor import atualizar_notificacoes_professor
import flet as ft
from database.db import buscar_usuario_por_matricula, registrar_acao


def solicitar_chave(matricula, senha, page):
    usuario = buscar_usuario_por_matricula(matricula, senha)

    if not usuario:
        page.snack_bar = ft.SnackBar(
            ft.Text("Usuário não encontrado ou senha incorreta!"))
        page.snack_bar.open = True
        page.update()
        return

    aluno_id, nome, matricula, tipo, com_chave = usuario

    # Verificar se o aluno já tem a chave
    if com_chave:
        page.snack_bar = ft.SnackBar(ft.Text(f"{nome} já está com a chave!"))
    else:
        registrar_acao(aluno_id, 'retirada')
        page.snack_bar = ft.SnackBar(
            ft.Text(f"{nome} retirou a chave com sucesso!"))

    page.snack_bar.open = True
    page.update()


def devolver_chave(matricula, senha, page):
    usuario = buscar_usuario_por_matricula(matricula, senha)

    if not usuario:
        page.snack_bar = ft.SnackBar(
            ft.Text("Usuário não encontrado ou senha incorreta!"))
        page.snack_bar.open = True
        page.update()
        return

    aluno_id, nome, matricula, tipo, com_chave = usuario

    # Verificar se o aluno realmente está com a chave
    if not com_chave:
        page.snack_bar = ft.SnackBar(ft.Text(f"{nome} não está com a chave!"))
    else:
        registrar_acao(aluno_id, 'devolucao')
        page.snack_bar = ft.SnackBar(
            ft.Text(f"{nome} devolveu a chave com sucesso!"))

    page.snack_bar.open = True
    page.update()


def confirmar_retirada(aluno_matricula, page):
    # Confirmação da retirada
    page.snack_bar = ft.SnackBar(
        ft.Text(f"Retirada confirmada para aluno: {aluno_matricula}"))
    page.snack_bar.open = True
    page.update()


def confirmar_devolucao(aluno_matricula, page):
    # Confirmação da devolução
    page.snack_bar = ft.SnackBar(
        ft.Text(f"Devolução confirmada para aluno: {aluno_matricula}"))
    page.snack_bar.open = True
    page.update()


def professor_view(page):
    notificacoes = ft.Text("Notificações:")

    # Exibir as notificações
    notificacoes_lista = ft.ListView(
        controls=[
            ft.Text(notificacao) for notificacao in notificacoes_professor
        ],
        spacing=10,
        padding=20
    )

    # Exibir o histórico
    historico_lista = ft.ListView(
        controls=[
            ft.Text(entry) for entry in historico_chaves
        ],
        spacing=10,
        padding=20
    )

    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Painel do Professor", size=30, weight="bold"),
                notificacoes,
                notificacoes_lista,
                ft.ElevatedButton(
                    "Atualizar Notificações", on_click=lambda e: atualizar_notificacoes_professor(page)),
                ft.Divider(height=50),  # Divisor para separar histórico
                ft.Text("Histórico de Chaves:"),
                historico_lista,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
