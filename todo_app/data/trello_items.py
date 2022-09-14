import requests, os, json, pymongo, dotenv
from pymongo import MongoClient
from requests import api
from todo_app.data.todoitem import ToDoItem
from requests.api import post
from bson import ObjectId
import certifi


ca = certifi.where()
connectionn_string = os.environ.get("PRIMARY_CONNECTION_STRING")
client = MongoClient(connectionn_string, tlsCAFile=ca)
db = client.todo_app
todo_cards = db.todo_tasks 


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
    print(response.text)
    return response.json()
    
# Part-2a: Module_10.  Replacing Trello
def get_all_cards():
    find_cards = todo_cards.find()
    todo_items = []
    for card in find_cards:
        id = card["_id"]
        title = card["title"]
        status = card["status"]
        item = ToDoItem(id, title, status)
        todo_items.append(item)

    return todo_items


# Part-2a: Module_10.  Replacing Trello
def create_trello_card(name):
    todo = {
    "title": name,
    "status": "Not Started"
    }

    todo_cards.insert_one(todo).inserted_id

# Part-4: Module_2. Function that marks item as complete
def complete_trello_card(id):
    todo = {
        "_id":ObjectId (id),
        }
    complete = { "$set":{ "status": "Completed" } }
    todo_cards.update_one( todo, complete)
    # completeing_card_url = f"http://api.trello.com/1/cards/{id}"

    # query_params_complete = {
    #     "key": os.environ.get("API_KEY"),
    #     "token": os.environ.get("API_TOKEN"),
    #     "idList": os.environ.get("COMPLETED_LIST"),
    #     "id": id,
    # }

    # return requests.put(completeing_card_url, params=query_params_complete)


# Function that transitions card to "In-Progress"
def in_progress_trello_card(id):
    todo = {
        "_id":ObjectId (id),
        }
    inprogress = { "$set":{ "status": "In-Progress" } }
    todo_cards.update_one( todo, inprogress)
    # card_in_progress_url = f"http://api.trello.com/1/cards/{id}"

    # query_params_in_progress = {
    #     "key": os.environ.get("API_KEY"),
    #     "token": os.environ.get("API_TOKEN"),
    #     "idList": os.environ.get("INPROGRESS_LIST"),
    #     "id": id,
    # }

    # return requests.put(card_in_progress_url, params=query_params_in_progress)

    # Function that delete's cards


def delete_card(id):
    todo = {
        "_id":ObjectId (id),
         }

    todo_cards.delete_one(todo)

