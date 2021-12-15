import requests, os, json
from requests import api

from requests.api import post

key = os.environ.get('API_KEY')
token = os.environ.get('API_TOKEN')
board = os.environ.get('BOARD')
nostarted_list = os.environ.get('NOTSTARTED_LIST')

main_trello_endpoint = "https://api.trello.com/1/"

# Function that curates the lists within a board
def get_trello_lists():
   reqUrl = f"http://api.trello.com/1/boards/{board}/lists"

   query_params = {
      "key": key,
      "token": token,
      "cards": "open"
   }

   response = requests.get(reqUrl, params = query_params)

   return response.json()

# Function that creates a new card
def create_trello_card(card_name, card_description):
    create_card_endpoint = main_trello_endpoint + "cards"
    jsonObj = {f"key ": {key}, "token": {token}, "idList": {nostarted_list},"name": card_name, "desc" : card_description}
    new_card = requests.post(create_card_endpoint, json=jsonObj)




