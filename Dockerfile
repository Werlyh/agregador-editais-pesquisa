FROM python:3.9-slim

# Instala locales para suporte a pt_BR
RUN apt-get update && apt-get install -y locales && \
    locale-gen pt_BR.UTF-8 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/entrypoint.sh

EXPOSE 10000

CMD ["/app/entrypoint.sh"]