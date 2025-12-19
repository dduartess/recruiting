# HDC Host - Landing Page e Sistema de Mensagens

Esse projeto é uma aplicação web full-stack desenvolvida com Django. A ideia principal é simular o site de uma empresa de hospedagem (HDC Host), contendo uma landing page para apresentação dos serviços e um painel administrativo interno para gerenciar os contatos recebidos.

O foco foi criar uma interface agradável e responsiva, mantendo o backend robusto e simples de manter.

## 🛠 Tecnologias

Nada de complicar o que pode ser simples. A stack escolhida foi:

*   **Django**: Cuida de todo o backend, rotas, ORM e autenticação.
*   **Tailwind CSS**: Para estilização rápida e responsiva (usado via CDN).
*   **Alpine.js**: Para gerenciar estados simples no frontend, como abrir e fechar modais de confirmação.
*   **HTMX**: Para interações dinâmicas sem precisar recarregar a página (ex: marcar mensagem como lida).
*   **SQLite**: Banco de dados padrão para desenvolvimento.

## 🚀 Funcionalidades

### Área Pública
*   **Landing Page**: Seções de Home, Preços e Contato.
*   **Formulário de Contato**: Envio de mensagens com validação e feedback visual (modais de sucesso/erro).

### Área Administrativa (Restrita)
*   **Autenticação**: Sistema de Login, Logout e Cadastro de novos administradores.
*   **Dashboard de Mensagens**: Lista todas as mensagens recebidas pelo site.
*   **Gestão de Leads**:
    *   Visualizar detalhes da mensagem.
    *   Alternar status de leitura (Lido/Não lido) dinamicamente.
    *   Editar informações do contato.
    *   Excluir mensagens (com modal de confirmação para evitar acidentes).

## 🏃‍♂️ Como rodar o projeto

Como o projeto usa Django padrão e CDNs para o frontend, é bem tranquilo de subir:

1.  **Clone o repositório e entre na pasta:**
    ```bash
    git clone <seu-repo>
    cd recruiting
    ```

2.  **Instale o Django:**
    ```bash
    pip install django
    ```

3.  **Prepare o banco de dados e rode o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

Agora é só acessar `http://127.0.0.1:8000`. Para acessar o painel, vá em "Entrar" e crie uma conta na opção de cadastro.