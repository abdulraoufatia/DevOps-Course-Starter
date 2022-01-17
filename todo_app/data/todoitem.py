# Part-5: Module_2. Creating a Class for 'To-do' Items
class ToDoItem:
   def __init__(self, id, title, status):
       self.id = id
       self.title = title
       self.status = status

# Module 3, Part 1: Step 1
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

# Module 3, Part 1: Step 2
    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item.status == "Not Started":
                todo_items.append(item)
        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == "In Progress":
                doing_items.append(item)
        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == "Completed":
                done_items.append(item)
        return done_items