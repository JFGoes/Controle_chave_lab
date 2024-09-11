import flet as ft
from database.db import inserir_usuario
# Certifique-se de importar corretamente
from views.login_view import login_view


def admin_view(page, realizar_login):
    page.clean()

    # Dropdown para selecionar o tipo de usuário
    tipo_usuario = ft.Dropdown(
        label="Tipo de Usuário",
        options=[
            ft.dropdown.Option("Aluno"),
            ft.dropdown.Option("Professor"),
            ft.dropdown.Option("Guarda")
        ],
        # Atualiza a tela com os campos corretos
        on_change=lambda e: exibir_campos_usuario()
    )

    # Variável para armazenar o caminho da foto
    foto_selecionada = ft.TextField(label="Foto Selecionada", read_only=True)

    # FilePicker para carregar a foto
    def on_file_selected(e):
        if file_picker.result:
            # Pega o nome do arquivo da foto
            foto_selecionada.value = file_picker.result.files[0].name
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_selected)

    # Campos comuns
    nome_completo = ft.TextField(label="Nome Completo")
    nome_usuario = ft.TextField(label="Nome de Usuário")
    # Campo de entrada para o laboratório
    laboratorio = ft.TextField(label="Laboratório")

    # Campos específicos para alunos
    curso = ft.TextField(label="Curso")
    matricula = ft.TextField(label="Matrícula")
    rg = ft.TextField(label="RG")
    email = ft.TextField(label="Email")
    telefone = ft.TextField(label="Telefone")

    # Campos específicos para professores
    siape = ft.TextField(label="SIAPE")

    # Campos específicos para guardas
    rg_guarda = ft.TextField(label="RG")

    # Função para exibir os campos corretos conforme o tipo de usuário selecionado
    def exibir_campos_usuario():
        # Limpa os controles da página
        page.controls.clear()

        # Campos para todos os usuários
        controls = [
            ft.Text("Cadastro de Usuários", size=25, weight="bold"),
            tipo_usuario,  # Dropdown para escolher o tipo de usuário
            nome_completo,
            nome_usuario,
            telefone,
            email,
            foto_selecionada,  # Campo para mostrar a foto selecionada
            ft.ElevatedButton("Carregar Foto", on_click=lambda _: file_picker.pick_files(
                allowed_extensions=["jpg", "jpeg", "png"]))
        ]

        # Condicionalmente exibe os campos conforme o tipo de usuário
        if tipo_usuario.value == "Aluno":
            controls.extend(
                [curso, matricula, rg, laboratorio])
        elif tipo_usuario.value == "Professor":
            controls.extend([siape, laboratorio])
        elif tipo_usuario.value == "Guarda":
            controls.extend([rg_guarda])

        # Botão para efetuar o cadastro e botão para sair
        controls.extend([
            ft.ElevatedButton("Cadastrar Usuário", on_click=cadastrar_usuario),
            ft.ElevatedButton("Sair", on_click=lambda _: login_view(
                page, realizar_login))  # Botão de sair
        ])

        # Atualiza a página com os novos controles
        page.add(ft.Column(controls, alignment=ft.MainAxisAlignment.CENTER,
                 horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        page.update()

    # Função para cadastrar usuário
    def cadastrar_usuario(e):
        # Verifica o tipo de usuário selecionado
        if tipo_usuario.value == "Aluno":
            inserir_usuario(
                nome_completo=nome_completo.value,
                nome_usuario=nome_usuario.value,
                curso=curso.value,
                matricula=matricula.value,
                rg=rg.value,
                email=email.value,
                telefone=telefone.value,
                laboratorio=laboratorio.value,  # Agora usa o campo de texto para laboratório
                tipo="Aluno",
                foto=foto_selecionada.value  # Foto carregada
            )
        elif tipo_usuario.value == "Professor":
            inserir_usuario(
                nome_completo=nome_completo.value,
                nome_usuario=nome_usuario.value,
                curso=curso.value,
                matricula=siape.value,  # SIAPE para professores
                rg=None,  # Professores não têm RG nesse exemplo
                email=email.value,
                telefone=telefone.value,
                laboratorio=laboratorio.value,  # Agora usa o campo de texto para laboratório
                tipo="Professor",
                foto=foto_selecionada.value  # Foto carregada
            )
        elif tipo_usuario.value == "Guarda":
            inserir_usuario(
                nome_completo=nome_completo.value,
                nome_usuario=nome_usuario.value,
                curso=None,  # Guardas não têm curso
                matricula=None,  # Guardas não têm matrícula
                rg=rg_guarda.value,
                email=email.value,
                telefone=telefone.value,
                tipo="Guarda",
                foto=foto_selecionada.value  # Foto carregada
            )

        # Exibe mensagem de sucesso e limpa os campos
        page.snack_bar = ft.SnackBar(
            ft.Text(f"{nome_completo.value} cadastrado com sucesso!"))
        page.snack_bar.open = True
        limpar_campos()
        page.update()

    # Função para limpar campos após o cadastro
    def limpar_campos():
        nome_completo.value = ""
        nome_usuario.value = ""
        curso.value = ""
        matricula.value = ""
        rg.value = ""
        email.value = ""
        telefone.value = ""
        siape.value = ""
        rg_guarda.value = ""
        laboratorio.value = ""  # Limpa o campo de texto do laboratório
        foto_selecionada.value = ""

    # Inicializa os campos
    exibir_campos_usuario()  # Mostra os campos iniciais de acordo com o tipo de usuário

    # Adiciona o FilePicker na página
    page.overlay.append(file_picker)
    page.update()
