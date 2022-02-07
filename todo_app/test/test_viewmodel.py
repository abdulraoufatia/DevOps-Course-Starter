from todo_app.data.todoitem import ToDoItem
from todo_app.data.viewmodel import ViewModel


def test_todo_items():
    items = [
        ToDoItem(1, "A New Todo", "Not Started"),
        ToDoItem(2, "A Working Todo", "In Progress"),
        ToDoItem(3, "A Completed Todo", "Completed"),
    ]
    viewmodel = ViewModel(items)
    todo_items = viewmodel.todo_items
    assert len(todo_items) == 1
    assert todo_items[0].status == "Not Started"


def test_doing_items():
    items = [
        ToDoItem(1, "A New Todo", "Not Started"),
        ToDoItem(2, "A Working Todo", "In Progress"),
        ToDoItem(3, "A Completed Todo", "Completed"),
    ]
    viewmodel = ViewModel(items)
    doing_items = viewmodel.doing_items
    assert len(doing_items) == 1
    assert doing_items[0].status == "In Progress"


def test_done_items():
    items = [
        ToDoItem(1, "A New Todo", "Not Started"),
        ToDoItem(2, "A Working Todo", "In Progress"),
        ToDoItem(3, "A Completed Todo", "Completed"),
    ]
    viewmodel = ViewModel(items)
    done_items = viewmodel.done_items
    assert len(done_items) == 1
    assert done_items[0].status == "Completed"
