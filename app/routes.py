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
def rodar_scraper_manual():
    print("Recebida requisição para rodar o scraper manualmente...")
    try:
        rodar_todos_scrapers()
        # Após rodar, explicitamente fazemos o commit final.
        # Embora o scraper já faça isso, é uma garantia extra.
        db.session.commit()
        print("Scraper executado e commit da sessão principal efetuado.")
        return "Scraper executado com sucesso! Verifique a página inicial em alguns instantes."
    except Exception as e:
        # Se algo der errado, desfazemos qualquer mudança pendente.
        db.session.rollback()
        print(f"Erro ao rodar scraper manualmente: {e}")
        return f"Ocorreu um erro ao executar o scraper: {e}"
    finally:
        # Garante que a sessão seja fechada, liberando a conexão com o banco.
        db.session.close()
        print("Sessão do banco de dados fechada.")