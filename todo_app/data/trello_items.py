import requests, os, json
from requests import api
from todo_app.data.todoitem import ToDoItem
from requests.api import post

# Part-3a: Module_2. Function that curates the lists within a board
def get_trello_lists():
    board = os.environ.get("BOARD")
    request_url =  f"http://api.trello.com/1/boards/{board}/lists"

    query_params = {
        "key": os.environ.get("API_KEY"),
        "token": os.environ.get("API_TOKEN"),
        "cards": "open",
    }

    response = requests.get(request_url, params=query_params)
    return response.json()


# Part-3b: Module_2.  Function that creates a new card.
def create_trello_card(name):
    create_card_url = "https://api.trello.com/1/cards"

    create_card_query_params = {
        "key": os.environ.get("API_KEY"),
        "token": os.environ.get("API_TOKEN"),
        "idList": os.environ.get("NOTSTARTED_LIST"),
        "name": name,
    }
    return requests.post(create_card_url, params=create_card_query_params)


# Part-4: Module_2. Function that marks item as complete
def complete_trello_card(id):
    completeing_card_url = f"http://api.trello.com/1/cards/{id}"

    query_params_complete = {
        "key": os.environ.get("API_KEY"),
        "token": os.environ.get("API_TOKEN"),
        "idList": os.environ.get("COMPLETED_LIST"),
        "id": id,
    }

    return requests.put(completeing_card_url, params=query_params_complete)


# Function that transitions card to "In-Progress"
def in_progress_trello_card(id):
    card_in_progress_url = f"http://api.trello.com/1/cards/{id}"

    query_params_in_progress = {
        "key": os.environ.get("API_KEY"),
        "token": os.environ.get("API_TOKEN"),
        "idList": os.environ.get("INPROGRESS_LIST"),
        "id": id,
    }

    return requests.put(card_in_progress_url, params=query_params_in_progress)

    # Function that delete's cards


def delete_card(id):
    deleting_card = f"http://api.trello.com/1/cards/{id}"

    query_params_delete_card = {
        "key": os.environ.get("API_KEY"),
        "token": os.environ.get("API_TOKEN"),
        "id": id,
    }

    return requests.delete(deleting_card, params=query_params_delete_card)
