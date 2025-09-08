FROM python:3.9-slim

# Instala dependências necessárias incluindo locales
RUN apt-get update && apt-get install -y \
    locales \
    && rm -rf /var/lib/apt/lists/*

# Gera as locales pt_BR
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8

# Configura as variáveis de ambiente
ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
ENV LC_TIME pt_BR.UTF-8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

EXPOSE 10000

CMD ["/app/entrypoint.sh"]