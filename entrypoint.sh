#!/bin/sh

# Seta a variável de ambiente para o Flask
export FLASK_APP=run.py

# Aplica qualquer migração de banco de dados pendente
echo "Aplicando migrações do banco de dados..."
flask db upgrade

# Inicia o servidor Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn --bind 0.0.0.0:10000 --workers 2 run:app 