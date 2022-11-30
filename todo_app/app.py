from os import name
from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.mongo_items import MongoClient
from todo_app.flask_config import Config
from todo_app.data.todoitem import ToDoItem
from todo_app.data.viewmodel import ViewModel
from flask_login import LoginManager, login_required, login_user, current_user
import os, requests
from todo_app.data.user import User
from werkzeug.exceptions import Forbidden

client_id='CLIENTID'
client_secret='CLIENTSECRET'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.config['LOGIN_DISABLED'] = os.getenv('LOGIN_DISABLED') == 'True'
    login_manager = LoginManager()

    mongo_client = MongoClient()

    # Part 1, Step 1 - Module_3: Making a ViewModel
    @app.route("/", methods=["GET"])
    @login_required
    def index():
        todo_items = mongo_client.get_all_cards()
        # Part 1, Step 1 - Module_3: Making a ViewModel
        view_model = ViewModel(todo_items, current_user)
        return render_template("index.html", view_model=view_model)

    @app.route("/newitem", methods=["POST"])
    @login_required
    def new_item():
        if current_user.writer_role():
            item = request.form["todo"]
            mongo_client.create_mongo_item(item)
        else:
            raise Forbidden("Access denied")
        return redirect("/")

    @app.route("/in_progress", methods=["POST"])
    @login_required
    def mark_item_in_progress():
        if current_user.writer_role():
            id = request.form.get("inprogress")
            mongo_client.in_progress_mongo_item(id)
        else:
            raise Forbidden("You are not allowed to be here!")
        return redirect("/")

    @app.route("/complete_item", methods=["POST"])
    @login_required
    def complete_item():
        if current_user.writer_role():
            if request.method == "POST":
                id = request.form["id"]
                mongo_client.complete_mongo_item(id)
                return redirect(url_for("index"))
            else:
                return render_template()
        else:
            raise Forbidden("Access denied")
        return redirect("/")

    @app.route("/delete_card", methods=["POST"])
    @login_required
    def deleting_card_function():
        if current_user.writer_role():
            delete_card = request.form["delete_card"]
            mongo_client.delete_item(delete_card)
        else:
            raise Forbidden("Access denied")
        return redirect("/")

    @login_manager.unauthorized_handler
    def unauthenticated():
        return redirect ('https://github.com/login/oauth/authorize?client_id='+ os.getenv(client_id))
    
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)
    login_manager.init_app(app)

    @app.route('/login/callback')
    def login():
        code= request.args.get('code')
        access_token_url = 'https://github.com/login/oauth/access_token'
        payload = {
            'client_id': os.getenv(client_id),
            'client_secret': os.getenv(client_secret),
            'code': code,
        } 
        r = requests.post(access_token_url, json=payload, headers={'Accept': 'application/json'})
        access_token = r.json().get('access_token')
        print(access_token)
        reqUrl = "https://api.github.com/user"

        headersList = {
        "Accept": "*/*",
        "Authorization": f"Bearer {access_token}" 
        }

        response = requests.get(reqUrl, headers=headersList)

        response_json = response.json()
        user = User(response_json['login'])

        login_user(user)
        return redirect('/')


    return app


if __name__ == "__main__":
    create_app(create_app).run()
