from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)

def test_read_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_return_item():
    item_data = {"name": "Test Item", "description": "This is a test item", "value": 42}
    response = client.post("/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_return_item_without_description():
    item_data = {"name": "Test Item", "value": 42}
    response = client.post("/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "description": None, "value": 42}

