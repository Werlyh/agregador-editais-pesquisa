from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Edital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False, unique=True)
    agencia = db.Column(db.String(50), nullable=False)
    data_limite = db.Column(db.Date, nullable=True)
    data_publicacao = db.Column(db.DateTime, default=datetime.utcnow)
    favorito = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Edital {self.titulo}>'