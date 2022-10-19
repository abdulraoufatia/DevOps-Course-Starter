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

# Part-2a: Module_10.  Replacing Trello: Transitions cards to "Complete" status
def complete_trello_card(id):
    todo = {
        "_id":ObjectId (id),
        }
    complete = { "$set":{ "status": "Completed" } }
    todo_cards.update_one( todo, complete)

# Part-2a: Module_10.  Replacing Trello: Transitions cards to "In-Progress" status
def in_progress_trello_card(id):
    todo = {
        "_id":ObjectId (id),
        }
    inprogress = { "$set":{ "status": "In-Progress" } }
    todo_cards.update_one( todo, inprogress)


def delete_card(id):
    todo = {
        "_id":ObjectId (id),
         }

    todo_cards.delete_one(todo)

