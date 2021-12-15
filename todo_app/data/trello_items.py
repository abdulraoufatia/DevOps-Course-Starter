import requests, os, json
from requests import api

from requests.api import post

key = os.environ.get('API_KEY')
token = os.environ.get('API_TOKEN')
board = os.environ.get('BOARD')
list_id = os.environ.get('NOTSTARTED_LIST')

main_trello_endpoint = "https://api.trello.com/1/"

# Function that curates the lists within a board
def get_trello_lists():
   reqUrl = f"http://api.trello.com/1/boards/{board}/lists"

   query_params = {
      "key": key,
      "token": token,
      "cards": "open"
   }

   return requests.get(reqUrl, params=query_params).json()

# Function that creates a new card
def create_trello_card(name):
   create_card_url = "https://api.trello.com/1/cards"

   create_card_query_params = {
      "key": key,
      "token": token,
      "idList": list_id,
      "name": name
   }
   return requests.post(create_card_url, params = create_card_query_params)
   # response = requests.post(create_card_url, params = create_card_query_params)

# Function that marks item as complete
def complete_item(id):
   completeing_card_url = f"http://api.trello.com/1/cards{id}"

   query_params_complete = {
      "key": key,
      "token": token,
      "cards": "closed",
      "id" : id
      
   }
   
   return requests.put(completeing_card_url, params = query_params_complete)

   # response = requests.get(completeing_card_url, params = query_params)
   # print(response.text)
