import requests, os, json
from requests import api

from requests.api import post

key = os.environ.get('API_KEY')
token = os.environ.get('API_TOKEN')
board = os.environ.get('BOARD')
not_started_list_id = os.environ.get('NOTSTARTED_LIST')
in_progress_list_id = os.environ.get('INPROGRESS_LIST')
completed_list_id = os.environ.get('COMPLETED_LIST')

# Part-3a: Module_2. Function that curates the lists within a board
def get_trello_lists():
   request_url = f"http://api.trello.com/1/boards/{board}/lists"

   query_params = {
      "key": key,
      "token": token,
      "cards": "open"
   }

   return requests.get(request_url, params=query_params).json()

# Part-3b: Module_2.  Function that creates a new card.  
def create_trello_card(name):
   create_card_url = "https://api.trello.com/1/cards"

   create_card_query_params = {
      "key": key,
      "token": token,
      "idList": not_started_list_id,
      "name": name
   }
   return requests.post(create_card_url, params = create_card_query_params)
   #response = requests.post(create_card_url, params = create_card_query_params)
# Part-4: Module_2. Function that marks item as complete
def complete_trello_card(id, completed_list_id):
   completeing_card_url = f"http://api.trello.com/1/cards/{id}"

   query_params_complete = {
      "key": key,
      "token": token,
      "idList": completed_list_id,
      "id" : id
      
   }
   
   return requests.put(completeing_card_url, params = query_params_complete)

# Function that transitions card to "In-Progress"
def in_progress_trello_card(id, in_progress_list_id):
   card_in_progress_url = f"http://api.trello.com/1/cards/{id}"

   query_params_in_progress = {
      "key": key,
      "token": token,
      "idList": in_progress_list_id,
      "id" : id
   }

   return requests.put(card_in_progress_url, params = query_params_in_progress)