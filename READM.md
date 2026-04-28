🚀 TechNova - Lojinha de Eletrônicos
Bem-vindo ao TechNova, um sistema de gerenciamento de inventário desenvolvido com FastAPI e SQLAlchemy. Aqui você pode organizar seus produtos e categorias de eletrônicos de forma rápida e intuitiva.

🛠️ Tecnologias Utilizadas
Backend: FastAPI (Python 3.x)

Banco de Dados: SQLAlchemy (SQLite por padrão)

Templates: Jinja2 + HTML5/CSS3 (FontAwesome para ícones)

Servidor: Uvicorn

📋 Pré-requisitos
Antes de começar, você vai precisar ter o Python instalado em sua máquina. Depois, instale as dependências necessárias:

Bash

pip install fastapi sqlalchemy uvicorn jinja2 python-multipart
🚀 Como Executar o Projeto
Certifique-se de que os arquivos main.py, models.py e database.py estão na mesma pasta.

Garanta que a pasta templates/ contém os arquivos index.html e cadastrar.html.

No terminal, execute o comando:

Bash

uvicorn main:app --reload
Abra o navegador em: http://127.0.0.1:8000

🔐 Acesso ao Painel Administrativo (CRUD)
Para gerenciar a loja (adicionar, listar ou excluir categorias e produtos), você não precisa decorar URLs complexas.

Na página inicial (Home), olhe para o canto superior direito.

Clique no botão "Sou Administrador".

Você será redirecionado para o painel de gestão onde o "poder" está em suas mãos.

Nota: No painel administrativo, você pode cadastrar novas categorias (ex: Teclados, Mouses) e vincular produtos a elas, além de poder excluir itens obsoletos com apenas um clique.

📂 Estrutura do Projeto
Plaintext

├── main.py          # Rotas e lógica do FastAPI
├── models.py        # Definição das tabelas (Eletronico e Produto)
├── database.py      # Configuração da conexão com o Banco de Dados
├── templates/       # Arquivos HTML (Jinja2)
│   ├── index.html   # Vitrine de produtos
│   └── cadastrar.html # Painel Administrativo (CRUD)
└── lojinha.db       # Banco de dados SQLite (gerado automaticamente)
🤝 Contribuição
Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request se quiser melhorar o design ou adicionar novas funcionalidades (como um sistema de login real, né? Segurança em primeiro lugar! 😉).

Desenvolvido com ☕ e Python por um dev que não aguenta mais Erro 500.