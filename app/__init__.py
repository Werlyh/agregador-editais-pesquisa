from flask import Flask
from flask_migrate import Migrate
import os
from .models import db
from .scheduler import sched

migrate = Migrate()

def setup_database(app):
    with app.app_context():
        # Use Flask-Migrate em vez de create_all
        from flask_migrate import upgrade
        try:
            upgrade()
        except Exception as e:
            print(f"Erro ao executar migrations: {e}")
            # Fallback seguro
            inspector = db.inspect(db.engine)
            if not inspector.has_table('edital'):
                db.create_all()
def create_app():
    app = Flask(__name__)

    database_url = os.getenv('DATABASE_URL')
    if database_url:
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///editais.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   
    db.init_app(app)
    migrate.init_app(app, db)

    setup_database(app) 

    from . import routes
    app.register_blueprint(routes.main_bp)

    if not sched.running:
        sched.start()
        print("Agendador iniciado!")

    return app