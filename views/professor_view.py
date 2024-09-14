import flet as ft
# Função para listar o histórico no banco de dados
from database.db import listar_historico_chaves
from views.login_view import login_view
from database.db import buscar_historico_por_intervalo
from database.db import listar_historico_por_professor
from datetime import datetime

def professor_view(page, realizar_login):
    page.clean()

    # Campos para selecionar intervalo de datas
    data_inicio = ft.TextField(label="Data de Início (YYYY-MM-DD)")
    data_fim = ft.TextField(label="Data de Fim (YYYY-MM-DD)")

    # Função para carregar o histórico com base nas datas
    def carregar_historico(e):
        try:
            # Converte as strings de data em objetos datetime
            data_inicio_dt = datetime.strptime(data_inicio.value, '%Y-%m-%d')
            data_fim_dt = datetime.strptime(data_fim.value, '%Y-%m-%d')

            # Busca o histórico no intervalo
            historico = buscar_historico_por_intervalo(data_inicio_dt, data_fim_dt)

            # Limpar a tela antes de adicionar o histórico
            page.clean()

            if not historico:
                page.add(ft.Text("Nenhum registro de chaves encontrado nesse período."))
            else:
                for solicitacao in historico:
                    solicitacao_id, aluno_nome, chave_id, status, data_solicitacao = solicitacao
                    page.add(
                        ft.Row(
                            controls=[
                                ft.Text(f"Aluno: {aluno_nome} | Chave ID: {chave_id} | Status: {status} | Data: {data_solicitacao}")
                            ]
                        )
                    )

            # Botão para sair ou voltar
            page.add(ft.ElevatedButton("Voltar", on_click=lambda _: login_view(page, realizar_login)))
            page.update()

        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Datas inválidas. Use o formato YYYY-MM-DD."))
            page.snack_bar.open = True
            page.update()

    # Interface para o professor buscar o histórico
    page.add(ft.Text("Histórico de Chaves", size=30, weight="bold"))
    page.add(data_inicio)
    page.add(data_fim)
    page.add(ft.ElevatedButton("Buscar Histórico", on_click=carregar_historico))
    page.add(ft.ElevatedButton("Sair", on_click=lambda _: login_view(page, realizar_login)))

    page.update()

# def professor_view(page, realizar_login):
#     page.clean()
    
#     # Função para carregar e exibir o histórico de chaves
#     def carregar_historico():
#         historico = listar_historico_chaves()

#         # Limpar a página antes de adicionar novos elementos
#         page.clean()

#         # Verificar se há histórico
#         if not historico:
#             page.add(
#                 ft.Text("Nenhum histórico de solicitações de chaves encontrado."))
#         else:
#             for solicitacao in historico:
#                 solicitacao_id, aluno_nome, chave_id, status, data_solicitacao = solicitacao
#                 page.add(
#                     ft.Row(
#                         controls=[
#                             ft.Text(f"Aluno: {aluno_nome} | Chave ID: {chave_id} | Status: {
#                                     status} | Data: {data_solicitacao}")
#                         ]
#                     )
#                 )

#         # Botão para voltar ou sair
#         page.add(ft.ElevatedButton(
#             "Sair", on_click=lambda _: login_view(page, realizar_login)))
#         page.update()

#     # Carregar a interface principal do professor
#     page.add(ft.Text("Histórico de Chaves", size=30, weight="bold"))

#     # Chama a função para carregar o histórico
#     carregar_historico()

#     page.update()

# def professor_view(page):
#     page.clean()

#     # Função para carregar o histórico do banco de dados
#     def carregar_historico():
#         # Função que retorna uma lista de ações do histórico
#         historico = listar_historico_chaves()

#         # Limpar a página antes de adicionar novos elementos
#         page.clean()

#         if not historico:
#             # Caso o histórico esteja vazio, exibe uma mensagem
#             return [ft.Text("Nenhum registro encontrado.", size=20)]
#         return [
#             ft.Text(f"Ação: {
#                     entry['acao']} - Aluno: {entry['aluno']} - Horário: {entry['timestamp']}")
#             for entry in historico
#         ]

#     # Função para atualizar as notificações e o histórico
#     def atualizar_historico(e):
#         page.controls.clear()
#         page.add(
#             ft.Column(
#                 controls=[
#                     ft.Text("Histórico de Chaves", size=25, weight="bold"),
#                     *carregar_historico(),  # Carrega as ações de retirada e devolução
#                     ft.ElevatedButton("Atualizar Histórico",
#                                       on_click=atualizar_historico),
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             )
#         )
#         page.update()

#     # Exibe a interface inicial com um botão para atualizar o histórico
#     page.add(
#         ft.Column(
#             controls=[
#                 ft.Text("Painel do Professor", size=30, weight="bold"),
#                 ft.ElevatedButton("Atualizar Histórico",
#                                   on_click=atualizar_historico),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         )
#     )
#     page.update()

#     # Carregar o histórico ao iniciar
#     atualizar_historico(None)
