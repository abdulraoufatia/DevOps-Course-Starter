from flask import Flask, render_template, request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

from todo_app.data.session_items import get_items 

@app.route('/', methods=['GET','POST'])
def index():
    get_items = ['item1','item2','item3']
    if request.method == 'POST':
        return do_the_login()
    return render_template('index.html', get_items=get_items)
