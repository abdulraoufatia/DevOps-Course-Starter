from flask.templating import render_template
from todo_app.data.todoitem import ToDoItem 
import json

with open("trello_response.json") as response_file:
    trello_lists = json.loads(response_file.read())

    item = ToDoItem(1, "new to-do item", "Not Started")
    item = []
    for list in trello_lists:
            for card in list['cards']:
                item.id
                item.title
                item.status

                item.append(item)

                item = ToDoItem(id = item.id, title = item.title, status=item.status)
# return render_template('index.html', todo_item = todo_items)
    print(item)

