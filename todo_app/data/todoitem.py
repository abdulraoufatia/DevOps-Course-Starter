# Part-5: Module_2. Creating a Class for 'To-do' Items
class ToDoItem:
   def __init__(self, id, title, status):
       self.id = id
       self.title = title
       self.status = status

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items