from dotenv import load_dotenv, find_dotenv
from todo_app import app
import mongomock
import pytest

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    # Arrange - MISSING!
    create_mongo_item = 
    create_mongo_item("Test card")
   
    
    # Act
    response = client.get("/")

    # Assert 
    assert response.status_code == 200
    assert "Test card" in response.data.decode()