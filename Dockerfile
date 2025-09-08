# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando padrão para iniciar o servidor, sem o entrypoint
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "2", "run:app"]