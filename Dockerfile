# Use a imagem oficial com Python 3.11
FROM python:3.11-slim

# Evita criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que o log seja mostrado no console
ENV PYTHONUNBUFFERED=1

# Instala pacotes necessários ao sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório padrão do app
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Comando de inicialização (ajuste se seu app for diferente)
CMD ["python", "consult.py"]