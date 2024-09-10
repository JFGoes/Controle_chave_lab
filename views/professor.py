import flet as ft
from controllers.dados import notificacoes_professor, historico_chaves

def atualizar_notificacoes_professor(page):
    # Atualiza a tela do professor com as notificações mais recentes
    page.snack_bar = ft.SnackBar(ft.Text("Notificações atualizadas"))
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
                ft.ElevatedButton("Atualizar Notificações", on_click=lambda e: atualizar_notificacoes_professor(page)),
                ft.Divider(height=50),  # Divisor para separar histórico
                ft.Text("Histórico de Chaves:"),
                historico_lista,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
