from os import name
from flask import Flask, render_template, request, redirect, url_for
from tomlkit import item
from todo_app.data.trello_items import (
    get_trello_lists,
    create_trello_card,
    complete_trello_card,
    completed_list_id,
    in_progress_trello_card,
    in_progress_list_id
)
from todo_app.flask_config import Config
from todo_app.data.todoitem import ToDoItem, ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    # Part 1, Step 1 - Module_3: Making a ViewModel
    @app.route("/", methods=["GET"])
    def index():
        view_model = get_trello_lists()
        # Part 5 - Module_2: Creating a class for 'to-do' items
        trello_lists = get_trello_lists()
        todo_items = []
        for list in trello_lists:
            for card in list["cards"]:
                id = card["id"]
                title = card["name"]
                status = list["name"]
                item = ToDoItem(id, title, status)
                todo_items.append(item)
        # Part 1, Step 1 - Module_3: Making a ViewModel
        view_model = ViewModel(todo_items)
        return render_template("index.html", view_model=view_model)

    @app.route("/newitem", methods=["POST"])
    def new_item():
        item = request.form["todo"]
        create_trello_card(item)
        return redirect(url_for("index"))

    @app.route("/in_progress", methods=["POST"])
    def mark_item_in_progress():
        id = request.form.get("inprogress")
        in_progress_trello_card(id, in_progress_list_id)
        return redirect(url_for("index"))

    @app.route("/complete_item", methods=["POST"])
    def complete_item():
        if request.method == "POST":
            id = request.form["id"]
            complete_trello_card(id, completed_list_id)
            return redirect(url_for("index"))
        else:
            return render_template()

    @app.route("/delete_card", methods=["POST"])
    def deleting_card_function():
        delete_item = request.form["deleting_card_form"]
        deleting_card_function(delete_item)
        return redirect(url_for("index"))

    # if __name__ == "__main__":
    #     create_app().run()