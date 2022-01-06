from os import name
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.datastructures import ResponseCacheControl
from todo_app.data.trello_items import get_trello_lists, create_trello_card, complete_trello_card, completed_list_id
from todo_app.flask_config import Config
from todo_app.data.todoitem import ToDoItem

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods = ['GET'])
def index():
    item = ToDoItem(1, "new to-do item", "Not Started")
    item= []
    for list in item:
        for item in list['name']:
            item.id
            item.title
            item.status
            item.append(item)
            item = ToDoItem(id = item.id, title = item.title, status=item.status)
    return render_template('index.html' , item = item)

# def index():
#     trello_lists = get_trello_lists()
#     todo_items = []
#     for list in trello_lists:
#         for card in list['cards']:
#             todo_items.append(card)
#     return render_template('index.html' , todo_items = todo_items)
    

@app.route('/newitem', methods = ['POST'])
def new_item():
    item = request.form['todo']
    create_trello_card(item)
    return redirect(url_for('index'))

@app.route('/complete_item', methods = ['POST'])
def complete_item():
    if request.method == 'POST':
        id = request.form['id']
        complete_trello_card(id, completed_list_id)
        return redirect(url_for('index'))
    else:
        return render_template()
