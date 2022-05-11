import os
from threading import Thread
from todo_app import app
from todo_app.data.trello_items import create_trello_board, delete_trello_board
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver



@pytest.fixture(scope='module')
def app_with_temp_board():

    file_path = find_dotenv(".env")
    load_dotenv(file_path, override=True)

    board_id = create_trello_board('Module_3_Board_Sel.')    # Create the new board & update the board id environment variable
    os.environ['BOARD'] = board_id

    application = app.create_app() # construct the new application
    
    thread = Thread(target=lambda: application.run(use_reloader=False)) # start the app in its own thread.
    thread.daemon = True
    thread.start()
    yield application
    
    thread.join(1) # Tear Down
    delete_trello_board(board_id)

def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'
