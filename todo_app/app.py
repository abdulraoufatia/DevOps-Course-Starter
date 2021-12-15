from os import name
from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import add_item
from todo_app.data.trello_items import get_trello_lists, create_trello_card, complete_item
from todo_app.flask_config import Config
from todo_app.data import trello_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods = ['GET'])
def index():
    trello_lists = get_trello_lists()
    todo_items = []
    for list in trello_lists:
        for card in list['cards']:
            todo_items.append(card)
    return render_template('index.html' , todo_items = todo_items)
    

@app.route('/newitem', methods = ['POST'])
def new_item():
    new_trello_card = create_trello_card(name) # - assinging the create_trello_card functions from trello_items.py to a variable in app.py
    cards = []
    for item in new_trello_card:
        cards.append(item['id'],item['idList'],item['name'])
    # item = request.form['todo']
    # additem = add_item(item)
    return redirect(url_for('index.html', cards=cards))

@app.route('/complete_item/<id>', methods = ['POST'])
def complete_item(id):
    id = request.args['id']
    return redirect('/')