#!/bin/sh

# Seta a variável de ambiente para o Flask funcionar
export FLASK_APP=run.py

# Aplica as migrações do banco de dados automaticamente
echo "Aplicando migrações do banco de dados..."
flask db upgrade

# Inicia o servidor principal da aplicação
echo "Iniciando Gunicorn..."
gunicorn --bind 0.0.0.0:10000 --workers 2 run:app