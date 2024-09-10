# KeyLab - Sistema de Controle de Chaves do Laboratório

**KeyLab** é um sistema simples e eficiente para o controle de retirada e devolução de chaves de laboratórios em universidades. O sistema permite que alunos retirem e devolvam chaves, ao mesmo tempo que garante que o controle é feito pelo guarda e monitorado pelos professores responsáveis. O sistema também conta com um administrador que gerencia o cadastro de usuários (alunos, professores e guardas) e laboratórios.

## Funcionalidades

### Usuários

O sistema permite o cadastro e gerenciamento de três tipos de usuários:

1. **Admin**:
   - Gerencia o sistema, cadastrando laboratórios, alunos, professores e guardas.
   - Acessa o painel de administração para ver e gerenciar todos os cadastros.
   
2. **Aluno**:
   - Pode solicitar a chave do laboratório.
   - Pode devolver a chave do laboratório.
   - As ações de retirada e devolução são registradas no sistema.
   
3. **Guarda**:
   - Confirma a retirada e a devolução da chave.
   - Controla o processo físico de entrega e recebimento da chave.
   
4. **Professor**:
   - Recebe notificações quando um aluno retira ou devolve uma chave do laboratório.
   - Pode acessar o histórico de retirada e devolução.

### Laboratórios
- O administrador pode cadastrar novos laboratórios e associar alunos e professores a esses laboratórios.
- O sistema permite que cada aluno e professor seja vinculado a um laboratório específico.

### Histórico
- O sistema registra todas as ações de retirada e devolução de chaves, permitindo que o administrador e os professores visualizem o histórico.

## Estrutura do Projeto

```
/keylab
│
├── app.py  # Arquivo principal da aplicação
├── views
│   ├── login_view.py  # Tela de login
│   ├── aluno_view.py  # Tela do aluno para solicitar e devolver chaves
│   ├── guarda_view.py  # Tela do guarda para confirmar retirada e devolução
│   ├── professor_view.py  # Tela do professor para ver notificações e histórico
│   ├── admin_view.py  # Tela do administrador para cadastrar usuários e laboratórios
├── controllers
│   ├── autenticacao.py  # Funções de login e autenticação de usuários
│   ├── chave_controller.py  # Controle da lógica de retirada e devolução
│   └── dados.py  # Simulação de banco de dados com listas
└── database
    └── db.py  # Configuração e interação com o banco de dados SQLite
```

## Instalação

### Pré-requisitos

- Python 3.8 ou superior.
- Biblioteca `flet` para interfaces gráficas.
- Biblioteca `sqlite3` (já incluída no Python).

### Passos para Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/keylab.git
   cd keylab
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install flet
   ```

4. Execute o sistema:
   ```bash
   python app.py
   ```

### Inicializando o Banco de Dados

Na primeira vez que o sistema for executado, ele criará automaticamente o banco de dados SQLite e as tabelas necessárias.

## Uso

1. **Login:**
   - **Admin**: Pode fazer login usando as credenciais de administrador (padrão: `admin/admin123`).
   - **Aluno, Guarda, Professor**: Podem se autenticar com as suas respectivas credenciais.

2. **Admin:**
   - Ao fazer login como administrador, o painel de administração será exibido.
   - O administrador pode cadastrar novos laboratórios, alunos, professores e guardas.
   
3. **Aluno:**
   - O aluno pode solicitar a chave de um laboratório e, depois de usá-la, devolvê-la.

4. **Guarda:**
   - O guarda valida a retirada e devolução das chaves fisicamente.

5. **Professor:**
   - O professor recebe notificações quando um aluno retira ou devolve uma chave e pode consultar o histórico.

## Estrutura de Dados

### Tabelas:

1. **Usuarios**:
   - `id`: ID do usuário (chave primária).
   - `nome`: Nome do usuário.
   - `matricula`: Matrícula única do usuário.
   - `senha`: Senha do usuário.
   - `tipo`: Tipo de usuário (`Aluno`, `Professor`, `Guarda`, `Admin`).
   - `com_chave`: Booleano que indica se o aluno está com a chave.
   - `laboratorio_id`: ID do laboratório ao qual o usuário está associado (caso de alunos e professores).

2. **Laboratorios**:
   - `id`: ID do laboratório (chave primária).
   - `nome`: Nome único do laboratório.

3. **Historico**:
   - `id`: ID do registro no histórico (chave primária).
   - `aluno_id`: ID do aluno que retirou ou devolveu a chave.
   - `acao`: Ação realizada (`retirada` ou `devolucao`).
   - `timestamp`: Data e hora da ação.

## Funcionalidades Futuras

- Notificações em tempo real para o guarda e professor.
- Relatórios detalhados para o administrador.
- Sistema de lembretes automáticos para devolução de chaves.

## Contribuindo

Contribuições são bem-vindas! Se você deseja melhorar o sistema ou adicionar novas funcionalidades, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

