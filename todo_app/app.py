from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import add_item
from todo_app.data.trello_items import get_trello_lists, complete_item
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
    item = request.form.get['todo']
    additem = add_item(item)
    return redirect(url_for('index', additem = additem))

@app.route('/complete_item/<id>', methods = ['POST'])
def complete_item(id):
    id = request.args['id']
    return