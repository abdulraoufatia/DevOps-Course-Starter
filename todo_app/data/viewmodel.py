# Module 3, Part 1: Step 1
class ViewModel:
    def __init__(self, items, user):
        self._items = items
        self._user = user

    @property
    def items(self):
        return self._items

    @property
    def is_writer(self):
        return self._user.writer_role()

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