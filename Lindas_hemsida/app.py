from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Bok, Kund, Bestallning, BestallningsDetalj

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/lindasdb'

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

# Kör först 'flask db init'
# Kör sedan 'flask db migrate -m "Initial migration.'
# Kör sedan 'flask db upgrade'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bocker')
def bocker():
    all_books = Bok.query.all()
    return render_template("bocker.html", all_books=all_books)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/kunder')
def kunder():
    alla_kunder = Kund.query.all()
    return render_template("kunder.html", kunder=alla_kunder)


@app.route('/kund/<kundid>')
def kund(kundid):
    våran_kund = Kund.query.filter_by(id=kundid).first()
    kundens_beställningar = Bestallning.query.filter_by(kund_id=kundid).all()
    return render_template("kund.html", kund=våran_kund, )


@app.route('/search_kunder', methods=['POST'])
def search_kunder():
    data = request.json
    search_query = data['query']
    search_type = data['type']

    if search_type == 'namn':
        search_results = Kund.query.filter(Kund.namn.like(f"%{search_query}%")).all()
    elif search_type == 'adress':
        search_results = Kund.query.filter(Kund.adress.like(f"%{search_query}%")).all()
    elif search_type == 'telefonnummer':
        search_results = Kund.query.filter(Kund.telefonnummer.like(f"%{search_query}%")).all()
    else:
        search_results = []

    return jsonify([{'id': kund.id, 'name': kund.namn, 'address': kund.adress} for kund in search_results])  # Adjust fields as needed


if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data()

    app.run()
    