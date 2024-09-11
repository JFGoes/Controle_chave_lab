import flet as ft
from database.db import buscar_solicitacoes, atualizar_solicitacao

def guarda_view(page):
    page.clean()

    def aprovar_solicitacao(solicitacao_id):
        atualizar_solicitacao(solicitacao_id, "aprovada")
        page.snack_bar = ft.SnackBar(ft.Text(f"Solicitação {solicitacao_id} aprovada."))
        page.snack_bar.open = True
        page.update()

    def negar_solicitacao(solicitacao_id):
        atualizar_solicitacao(solicitacao_id, "negada")
        page.snack_bar = ft.SnackBar(ft.Text(f"Solicitação {solicitacao_id} negada."))
        page.snack_bar.open = True
        page.update()

    solicitacoes = buscar_solicitacoes()
    solicitacoes_lista = [
        ft.Text(f"Solicitação ID: {sol['id']} - Usuário: {sol['nome_usuario']} - Status: {sol['status']} - Data: {sol['data_solicitacao']}")
        for sol in solicitacoes
    ]

    page.add(
        ft.Column(
            controls=[
                ft.Text("Autorizar Solicitações de Chave", size=25, weight="bold"),
                *solicitacoes_lista,
                ft.ElevatedButton("Aprovar Solicitação 1", on_click=lambda e: aprovar_solicitacao(1)),
                ft.ElevatedButton("Negar Solicitação 1", on_click=lambda e: negar_solicitacao(1)),
                ft.ElevatedButton("Sair", on_click=lambda _: login_view(page))  # Botão de sair
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
