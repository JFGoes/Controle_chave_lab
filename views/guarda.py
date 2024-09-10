import flet as ft
from controllers.chave_controller import confirmar_retirada, confirmar_devolucao

def guarda_view(page):
    aluno_matricula = ft.TextField(label="Matrícula do Aluno", autofocus=True)
    
    def confirmar_retirada_clicked(e):
        confirmar_retirada(aluno_matricula.value, page)

    def confirmar_devolucao_clicked(e):
        confirmar_devolucao(aluno_matricula.value, page)

    page.clean()
    page.add(
        ft.Column(
            controls=[
                ft.Text("Controle de Retirada e Devolução", size=25, weight="bold"),
                aluno_matricula,
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Confirmar Retirada", on_click=confirmar_retirada_clicked),
                        ft.ElevatedButton("Confirmar Devolução", on_click=confirmar_devolucao_clicked),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()
