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
todo_items = db.todo_tasks 
    
# Part-2a: Module_10.  Replacing Trello
def get_all_cards():
    find_cards = todo_items.find()
    items = []
    for card in find_cards:
        id = card["_id"]
        title = card["title"]
        status = card["status"]
        item = ToDoItem(id, title, status)
        items.append(item)

    return items


# Part-2a: Module_10.  Replacing Trello
def create_mongo_item(name):
    todo = {
    "title": name,
    "status": "Not Started"
    }

    todo_items.insert_one(todo).inserted_id

# Part-2a: Module_10.  Replacing Trello: Transitions cards to "Complete" status
def complete_mongo_item(id):
    todo = {
        "_id":ObjectId (id),
        }
    complete = { "$set":{ "status": "Completed" } }
    todo_items.update_one( todo, complete)

# Part-2a: Module_10.  Replacing Trello: Transitions cards to "In-Progress" status
def in_progress_mongo_item(id):
    todo = {
        "_id":ObjectId (id),
        }
    inprogress = { "$set":{ "status": "In-Progress" } }
    todo_items.update_one( todo, inprogress)


def delete_item(id):
    todo = {
        "_id":ObjectId (id),
         }

    todo_items.delete_one(todo)

