from flask import Flask, render_template, request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item(title) 

@app.route('/',  methods=["POST", "GET"])
def index():
    get_items = ['item1','item2','item3']
    add_item(title=[1,2,3,4])
    if request.method == 'POST':
        return do_the_login()
    return render_template('index.html', get_items=get_items)
