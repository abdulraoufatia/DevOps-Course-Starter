from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

from todo_app.data.session_items import get_items

@app.route('/', methods = ['POST', 'GET'])
def index():
    request.form.get('title')
    return render_template('index.html', items = get_items())
