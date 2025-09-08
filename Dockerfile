FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Torna nosso script de inicialização executável
RUN chmod +x /app/entrypoint.sh

# Define o script como o comando de inicialização do container
ENTRYPOINT ["/app/entrypoint.sh"]