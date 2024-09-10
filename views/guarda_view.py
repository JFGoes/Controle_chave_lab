import flet as ft

def guarda_view(page):
    page.clean()

    # Campo para inserir a matrícula do aluno para confirmar retirada ou devolução
    matricula_input = ft.TextField(label="Matrícula do Aluno", autofocus=True)

    def confirmar_retirada(e):
        # Lógica para confirmar retirada da chave (pode ser ajustado para conectar ao banco de dados)
        page.snack_bar = ft.SnackBar(ft.Text(f"Retirada confirmada para matrícula: {matricula_input.value}"))
        page.snack_bar.open = True
        page.update()

    def confirmar_devolucao(e):
        # Lógica para confirmar devolução da chave (pode ser ajustado para conectar ao banco de dados)
        page.snack_bar = ft.SnackBar(ft.Text(f"Devolução confirmada para matrícula: {matricula_input.value}"))
        page.snack_bar.open = True
        page.update()

    # Interface do guarda com botões de confirmação de retirada e devolução
    page.add(
        ft.Column(
            controls=[
                ft.Text("Controle de Retirada e Devolução", size=25, weight="bold"),
                matricula_input,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Confirmar Retirada", on_click=confirmar_retirada),
                        ft.ElevatedButton("Confirmar Devolução", on_click=confirmar_devolucao),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
