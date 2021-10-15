from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods = ['POST', 'GET'])
def index():
    items = get_items()
    return render_template('index.html', items = items, get_items = get_items)

@app.route('/newitem', methods = ['POST'])
def new_item():
    item = request.form['todo']
    additem = add_item(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()