import flet as ft
from database.db import listar_relatorio_diario

def relatorio_diario_view(page):
    page.clean()

    # Carregar o relatório diário
    relatorio = listar_relatorio_diario()
    relatorio_lista = [ft.Text(f"{entry['acao']} - {entry['nome_usuario']} - {entry['data']}") for entry in relatorio]

    page.add(
        ft.Column(
            controls=[
                ft.Text("Relatório Diário de Solicitações e Devoluções", size=25, weight="bold"),
                *relatorio_lista,
                ft.ElevatedButton("Sair", on_click=lambda _: login_view(page))  # Botão de sair
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
