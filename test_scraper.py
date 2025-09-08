from app import create_app, db
from app.scraper import rodar_todos_scrapers

# Cria uma instância da nossa aplicação Flask
app = create_app()

# 'Empurra' um contexto de aplicação. 
# Isso permite que nosso script acesse coisas da aplicação, como o banco de dados 'db'.
with app.app_context():
    print("Criando tabelas do banco de dados (se não existirem)...")
    db.create_all() # Garante que a tabela 'edital' exista
    
    print("Iniciando o teste do scraper...")
    rodar_todos_scrapers()
    
    print("Teste do scraper concluído.")