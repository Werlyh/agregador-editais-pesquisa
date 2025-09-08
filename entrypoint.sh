#!/bin/bash

# Verifica e configura locale se necessário
if ! locale -a | grep -q "pt_BR.UTF-8"; then
    echo "Locale pt_BR.UTF-8 não encontrado, gerando..."
    sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen
    locale-gen pt_BR.UTF-8
    update-locale LANG=pt_BR.UTF-8
fi

export LANG=pt_BR.UTF-8
export LC_ALL=pt_BR.UTF-8

# Executa migrations
flask db upgrade

# Inicia a aplicação
exec gunicorn -b :10000 --access-logfile - --error-logfile - run:app