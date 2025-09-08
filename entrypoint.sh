#!/bin/bash

# Espera o banco de dados ficar pronto (se necessário)
# sleep 5

# Executa migrations
flask db upgrade

# Inicia a aplicação
exec gunicorn -b :10000 --access-logfile - --error-logfile - run:app