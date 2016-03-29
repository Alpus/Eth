from app import app
from flask import render_template, jsonify, request
from app.logic import cards
from app import forms

@app.route("/")
def index():
    cards_ad = cards.get_ad()
    cards_new = cards.get_new()
    cards_all = cards.get_all()
    add_game = forms.AddGame()

    return render_template('cards.html', add_game=add_game, cards_ad=cards_ad,
                            cards_new=cards_new, cards_all=cards_all)

@app.route('/add_game', methods = ['POST'])
def add_game():
    add_game = forms.AddGame()
    add_game.from_json(request.json)

    print (add_game.data)

    if add_game.validate():
        return jsonify(success='OK');
    else:
        return jsonify(success='ERR');

