from apscheduler.schedulers.background import BackgroundScheduler
from .scraper import rodar_todos_scrapers

sched = BackgroundScheduler(daemon=True)

def job_function():
    """
    Função que será executada pelo agendador.
    É preciso criar um contexto da aplicação para que o scraper
    possa acessar o banco de dados.
    """
    from . import create_app
    app = create_app()
    with app.app_context():
        print("Executando tarefa agendada de busca de editais...")
        rodar_todos_scrapers()

sched.add_job(job_function, 'interval', minutes=1)