import flet as ft
from database.db import buscar_solicitacoes_pendentes, atualizar_status_solicitacao


def guarda_view(page):
    solicitacoes = buscar_solicitacoes_pendentes()

    def aprovar_solicitacao(e, solicitacao_id):
        atualizar_status_solicitacao(solicitacao_id, 'Autorizado')
        page.snack_bar = ft.SnackBar(ft.Text("Solicitação aprovada!"))
        page.snack_bar.open = True
        page.update()

    def negar_solicitacao(e, solicitacao_id):
        atualizar_status_solicitacao(solicitacao_id, 'Negado')
        page.snack_bar = ft.SnackBar(ft.Text("Solicitação negada!"))
        page.snack_bar.open = True
        page.update()

    page.clean()

    for solicitacao in solicitacoes:
        solicitacao_id, aluno_nome, chave_id, data_solicitacao = solicitacao
        page.add(
            ft.Row(
                controls=[
                    ft.Text(f"Aluno: {aluno_nome} | Chave: {
                            chave_id} | Data: {data_solicitacao}"),
                    ft.ElevatedButton(
                        "Aprovar", on_click=lambda e: aprovar_solicitacao(e, solicitacao_id)),
                    ft.ElevatedButton(
                        "Negar", on_click=lambda e: negar_solicitacao(e, solicitacao_id)),
                ]
            )
        )

    page.update()
