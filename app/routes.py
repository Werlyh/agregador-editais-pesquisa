from .scraper import rodar_todos_scrapers
from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from .models import db, Edital

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
# app/routes.py

@main_bp.route('/rodar-scraper-manual-agora')
def rodar_scraper_manual():
    print("--- INICIANDO SCRAPER MANUALMENTE ---")
    try:
        # 1. Roda o scraper (que agora só adiciona à sessão)
        rodar_todos_scrapers()

        # 2. Verifica quantos itens estão pendentes para serem salvos
        itens_pendentes = len(db.session.new)
        print(f"Itens pendentes para salvar: {itens_pendentes}")

        # 3. Se houver itens, tenta salvar
        if itens_pendentes > 0:
            print("Tentando fazer o commit no banco de dados...")
            db.session.commit()
            print("--- COMMIT BEM-SUCEDIDO! ---")
            return f"Scraper executado. {itens_pendentes} novos itens salvos."
        else:
            print("Nenhum item novo encontrado para salvar.")
            return "Scraper executado. Nenhum item novo encontrado."

    except Exception as e:
        # 4. Se algo der muito errado, desfaz tudo
        print(f"!!! ERRO DURANTE A TRANSAÇÃO: {e}")
        db.session.rollback()
        return f"Ocorreu um erro ao executar o scraper: {e}"
    finally:
        # 5. Fecha a sessão para libertar a ligação
        db.session.close()
        print("--- SESSÃO FECHADA ---")