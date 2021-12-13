import requests, os, json

key = os.environ.get('API_KEY')
token = os.environ.get('API_TOKEN')
board = os.environ.get('BOARD')



def get_trello_lists():
   reqUrl = f"http://api.trello.com/1/boards/{board}/lists"

   query_params = {
      "key": "2591d3c40f7f00e1ab5e3f1c97ef347f",
      "token": "eea232d0a490da0ad15c7867d2756896a625384f20f26148e5e45a4185f2bb4e",
      "cards": "open"
   }

   response = requests.get(reqUrl, params = query_params)

   return response.json()

