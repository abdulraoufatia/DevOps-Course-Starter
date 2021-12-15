from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import add_item
from todo_app.data.trello_items import get_trello_lists, create_trello_card
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
    item = request.form['todo']
    additem = add_item(item)
    return redirect(url_for('index'))

@app.route('/create_trello_card', methods = ['POST'])
def new_card_on_trello():
    add_card = create_trello_card()
    return render_template('index.html' , add_card = add_card)

if __name__ == '__main__':
    app.run()