import flet as ft
from database.db import buscar_solicitacoes_pendentes, atualizar_status_solicitacao
from views.login_view import login_view


def guarda_view(page, realizar_login):
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

    if not solicitacoes:
        page.add(ft.Text("Nenhuma solicitação pendente."))
    else:
        for solicitacao in solicitacoes:
            solicitacao_id, aluno_nome, aluno_rg, aluno_laboratorio, chave_id, data_solicitacao = solicitacao
            page.add(
                ft.Row(
                    controls=[
                        ft.Text(f"Aluno: {aluno_nome}"),
                        ft.Text(f"RG: {aluno_rg}"),
                        ft.Text(f"Laboratório: {aluno_laboratorio}"),
                        ft.Text(f"Chave ID: {chave_id}"),
                        ft.Text(f"Data: {data_solicitacao}"),
                        ft.ElevatedButton(
                            "Aprovar", on_click=lambda e: aprovar_solicitacao(e, solicitacao_id)),
                        ft.ElevatedButton(
                            "Negar", on_click=lambda e: negar_solicitacao(e, solicitacao_id)),
                    ]
                )
            )
    page.add(ft.ElevatedButton(
        "Sair", on_click=lambda _: login_view(page, realizar_login)))
    page.update()
