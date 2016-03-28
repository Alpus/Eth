from app import app
from flask import render_template
from app.logic import cards

@app.route("/")
def index():
    cards_ad = cards.get_ad()
    cards_new = cards.get_new()
    cards_all = cards.get_all()

    return render_template('cards.html', cards_ad=cards_ad,
                            cards_new=cards_new, cards_all=cards_all)

@app.route('/login', methods=['POST'])
def add():
    pass