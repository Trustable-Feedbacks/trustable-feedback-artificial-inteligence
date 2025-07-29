FROM python:3.10-slim

WORKDIR /app

# Atualiza pip, setuptools e wheel
RUN pip install --upgrade pip setuptools wheel

# Copia o requirements.txt para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta que sua app vai usar (exemplo 5000)
EXPOSE 5000

# Comando para rodar sua aplicação - ajuste para seu script principal
CMD ["python", "consult.py"]