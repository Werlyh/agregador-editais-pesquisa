from flask import Flask
from .models import db
from .scheduler import sched

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///editais.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.main_bp)

    if not sched.running:
        sched.start()
        print("Agendador iniciado!")

    return app