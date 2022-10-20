from os import name
from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.mongo_items import (
    get_all_cards,
    create_mongo_item,
    complete_mongo_item,
    in_progress_mongo_item,
    delete_item,
)
from todo_app.flask_config import Config
from todo_app.data.todoitem import ToDoItem
from todo_app.data.viewmodel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # Part 1, Step 1 - Module_3: Making a ViewModel
    @app.route("/", methods=["GET"])
    def index():
        todo_items = get_all_cards()
        # Part 1, Step 1 - Module_3: Making a ViewModel
        view_model = ViewModel(todo_items)
        return render_template("index.html", view_model=view_model)

    @app.route("/newitem", methods=["POST"])
    def new_item():
        item = request.form["todo"]
        create_mongo_item(item)
        return redirect(url_for("index"))

    @app.route("/in_progress", methods=["POST"])
    def mark_item_in_progress():
        id = request.form.get("inprogress")
        in_progress_mongo_item(id)
        return redirect(url_for("index"))

    @app.route("/complete_item", methods=["POST"])
    def complete_item():
        if request.method == "POST":
            id = request.form["id"]
            complete_mongo_item(id)
            return redirect(url_for("index"))
        else:
            return render_template()

    @app.route("/delete_card", methods=["POST"])
    def deleting_card_function():
        delete_item = request.form["delete_card"]
        delete_item(delete_item)
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    create_app(create_app).run()
