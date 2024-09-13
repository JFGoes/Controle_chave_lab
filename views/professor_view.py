import flet as ft
# Função para listar o histórico no banco de dados
from database.db import listar_historico_chaves


def professor_view(page):
    page.clean()

    # Função para carregar o histórico do banco de dados
    def carregar_historico():
        # Função que retorna uma lista de ações do histórico
        historico = listar_historico_chaves()

        # Limpar a página antes de adicionar novos elementos
        page.clean()

        if not historico:
            # Caso o histórico esteja vazio, exibe uma mensagem
            return [ft.Text("Nenhum registro encontrado.", size=20)]
        return [
            ft.Text(f"Ação: {
                    entry['acao']} - Aluno: {entry['aluno']} - Horário: {entry['timestamp']}")
            for entry in historico
        ]

    # Função para atualizar as notificações e o histórico
    def atualizar_historico(e):
        page.controls.clear()
        page.add(
            ft.Column(
                controls=[
                    ft.Text("Histórico de Chaves", size=25, weight="bold"),
                    *carregar_historico(),  # Carrega as ações de retirada e devolução
                    ft.ElevatedButton("Atualizar Histórico",
                                      on_click=atualizar_historico),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    # Exibe a interface inicial com um botão para atualizar o histórico
    page.add(
        ft.Column(
            controls=[
                ft.Text("Painel do Professor", size=30, weight="bold"),
                ft.ElevatedButton("Atualizar Histórico",
                                  on_click=atualizar_historico),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

    # Carregar o histórico ao iniciar
    atualizar_historico(None)
