📖 Resumo de Cada Pasta/Arquivo

alembic/ → Scripts de migração do banco de dados (criar/alterar tabelas).

app/ → Pasta principal da aplicação.

core/ → Configurações centrais do projeto.

config.py → Variáveis de ambiente (DB URL, secret key etc.).

security.py → Funções de autenticação e geração de tokens (JWT).

models/ → Modelos do banco de dados (SQLAlchemy).

user.py → Usuários (login, senha, email).

transaction.py → Transações financeiras (receitas/despesas).

category.py → Categorias (alimentação, transporte, salário etc.).

report.py → Relatórios consolidados (ex: gastos por mês, saldo).

schemas/ → Estruturas de validação de dados (Pydantic).

user.py → Esquema de usuário (registro/login/retorno).

transaction.py → Esquema de transações.

category.py → Esquema de categorias.

report.py → Esquema de relatórios.

crud/ → Lógica de acesso ao banco (CRUD).

user.py → Operações de usuários.

transaction.py → Operações de transações.

category.py → Operações de categorias.

report.py → Operações de relatórios.

api/v1/ → Endpoints da API.

auth.py → Login e registro de usuários.

users.py → Gerenciamento de usuários.

transactions.py → CRUD de transações.

categories.py → CRUD de categorias.

reports.py → Relatórios financeiros.

main.py → Ponto de entrada da aplicação FastAPI.

tests/ → Testes automatizados (Pytest).

docker-compose.yml → Orquestração da API + banco de dados com Docker.

Dockerfile → Instruções para build da imagem Docker.

requirements.txt → Lista de dependências do projeto.

README.md → Documentação principal do projeto.