from .scraper import rodar_todos_scrapers
from flask import Blueprint, render_template, request, jsonify
from .models import Edital, db
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    agencia = request.args.get('agencia')
    favoritos_only = request.args.get('favoritos')

    query = Edital.query.order_by(Edital.data_limite.desc())

    if agencia:
        query = query.filter(Edital.agencia == agencia)

    if favoritos_only:
        query = query.filter(Edital.favorito == True)

    editais = query.all()
    agencias = db.session.query(Edital.agencia).distinct().all()

    return render_template('index.html', editais=editais, agencias=[a[0] for a in agencias])

@main_bp.route('/edital/<int:edital_id>/favoritar', methods=['POST'])
def favoritar_edital(edital_id):
    edital = Edital.query.get_or_404(edital_id)
    edital.favorito = not edital.favorito # Inverte o status de favorito
    db.session.commit()
    return jsonify({'status': 'success', 'novo_status': edital.favorito})

@main_bp.route('/rodar-scraper-manual-agora')
def rodar_scraper_manual():
    try:
        rodar_todos_scrapers()
        return "Scraper executado com sucesso! Verifique a página inicial."
    except Exception as e:
        return f"Ocorreu um erro ao executar o scraper: {e}"