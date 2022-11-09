import requests, os, json, pymongo, dotenv
import pymongo
from requests import api
from todo_app.data.todoitem import ToDoItem
from requests.api import post
from bson import ObjectId
import certifi

class MongoClient:
    def __init__(self):
        ca = certifi.where()
        connectionn_string = os.environ.get("PRIMARY_CONNECTION_STRING")
        client = pymongo.MongoClient(connectionn_string, tlsCAFile=ca)
        db = client.todo_app
        todo_items = db.todo_tasks 
        self.todo_items = todo_items

    
    # Part-2a: Module_10.  Replacing Trello
    def get_all_cards(self):
        find_cards = self.todo_items.find()
        items = []
        for card in find_cards:
            id = card["_id"]
            title = card["title"]
            status = card["status"]
            item = ToDoItem(id, title, status)
            items.append(item)

        return items


    # Part-2a: Module_10.  Replacing Trello
    def create_mongo_item(self, name):
        todo = {
        "title": name,
        "status": "Not Started"
        }

        self.todo_items.insert_one(todo).inserted_id

    # Part-2a: Module_10.  Replacing Trello: Transitions cards to "Complete" status
    def complete_mongo_item(self, id):
        todo = {
            "_id":ObjectId (id),
            }
        complete = { "$set":{ "status": "Completed" } }
        self.todo_items.update_one( todo, complete)

    # Part-2a: Module_10.  Replacing Trello: Transitions cards to "In-Progress" status
    def in_progress_mongo_item(self, id):
        todo = {
            "_id":ObjectId (id),
            }
        inprogress = { "$set":{ "status": "In-Progress" } }
        self.todo_items.update_one( todo, inprogress)


    def delete_item(self, id):
        todo = {
            "_id":ObjectId (id),
            }

        self.todo_items.delete_one(todo)

