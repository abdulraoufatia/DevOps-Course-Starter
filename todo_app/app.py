from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/', methods = ['POST', 'GET'])
def index():
    items = get_items()
    return render_template('index.html', items = items, get_items = get_items)

@app.route('/newitem', methods = ['POST'])
def add_item():
    if request.method == 'POST':
      item = request.form['nm']
      return redirect(url_for('success',add_item = add_item))
    else:
      user = request.args.get('nm')
      return redirect(url_for('success',add_item = add_item))
    
    return ()

if __name__ == '__main__':
    app.run()