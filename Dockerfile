FROM python:3.11-slim

# Instala dependências do sistema (ODBC + gcc)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia requirements primeiro
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]




# CODIGOS PARA DOCKERFILE :
    
# 📌 Buildar imagem

    # docker build -t minha_api .    --->  -t dá um nome/tag à imagem).

# 📌 Rodar container

    # docker run -d -p 8000:8000 --name FINANCE API    -d → modo "detached" (roda em segundo plano)

    # -p → mapeia porta (host:container)   --name → dá nome ao container


# 📌 Listar containers

    #   docker ps             containers rodando
    #   docker ps -a          todos containers (inclui parados)


# 📌 Parar / iniciar container

    # docker stop api
    # docker start api

# 📌 Remover container

    # docker rm api


# 📌 Remover imagem

    # docker rmi minha_api

# 📌 Entrar dentro do container

    # docker exec -it api bash  ---->   (-it dá terminal interativo, tipo SSH no container)

# 📌 Ver logs

    # docker logs -f api    ---> (-f = segue em tempo real)

# 📌 Atualizar container (rebuildar)

    # docker stop api
    # docker rm api
    # docker build -t minha_api .
    # docker run -d -p 8000:8000 --name api minha_api

# 📌 Subir containers

    # docker-compose up
    # docker-compose up -d   # em segundo plano

# 📌 Derrubar containers

    # docker-compose down

# 📌 Rebuildar (após mudar Dockerfile)

    # docker-compose up --build

# 📌 Escalar serviços

    # docker-compose up --scale api=3 -d   ---> (sobe 3 instâncias do serviço api)

# 📌 Logs de todos os serviços

    # docker-compose logs -f

# 📌 Rodar comando dentro do serviço

    # docker-compose exec api alembic upgrade head



 #   ⚡ Atalhos úteis no dia a dia

# Parar tudo

    # docker stop $(docker ps -q)


# Remover tudo parado

    # docker container prune


# Remover todas imagens não usadas

    # docker image prune -a


# Ver espaço usado pelo Docker

    # docker system df