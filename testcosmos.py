import pymongo
import os
import dotenv

dotenv.load_dotenv()


client = pymongo.MongoClient(os.getenv("PRIMARY_CONNECTION_STRING"))

db = client.project_database
collection = db.project_collection

todo = {
    "title": "Mongo Todo",
    "status": "Not Started"
}


collection.insert_one(todo)


documents = collection.find()