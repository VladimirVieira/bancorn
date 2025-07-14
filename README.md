# 💰 BancoRN

Sistema bancário simples via terminal. Este projeto tem como foco o uso adequado de controle de versão e boas práticas com Git e GitHub, conforme orientações da disciplina DIM0517 - Gerência de Configuração e Mudanças.

### 👥 Equipe
- Pablo Gustavo Fernandes Maia - [@Pablo1Gustavo](https://github.com/Pablo1Gustavo)
- Vladimir Vieira - [@VladimirVieira](https://github.com/VladimirVieira)

### Versionamento
- GitHub como plataforma de hospedagem
- Padrão de branches: GitLab Flow

### 🛠️ Ferramentas
- Linguagem: Python (3.13)
- Banco de dados: PostgreSQL

### 🚀 Configurar e executar o projeto

1. Certifique-se de ter o Python (3.13), (Poetry)[https://python-poetry.org/docs/] e Docker instalados em sua máquina.
2. Execute o comando `poetry shell` para entrar no ambiente isolado do projeto.
3. Execute `poetry install` para instalar as dependências do projeto.
4. Execyte `pre-commit install` para aplicar o hook de pre-commit configurado no projeto.
4. Configure um banco Postgresql em sua máquina ou use o localizado no `docker-compose.yaml`.
5. Copie o `.env.example` para um `.env` e configure as variáveis.
6. Execute o projeto diretamente com `python app.py` ou utlize tambem o `docker-compose.yaml`. 
