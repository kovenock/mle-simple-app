import requests
import pytest

BASE_URL = "http://localhost:80" # Can be overriden via CLI, see conftest.py

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    """Get base URL from command line options or use default."""
    return pytestconfig.option.base_url or BASE_URL

def test_get_hello(base_url):
    """Test the health check endpoint."""
    response = requests.get(f"{base_url}/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_post_item(base_url):
    """Test the POST endpoint."""
    item = {
        "name": "test_item",
        "description": "This is a test item",
        "value": 42
    }
    response = requests.post(f"{base_url}/", json=item)
    assert response.status_code == 200
    assert response.json() == item
