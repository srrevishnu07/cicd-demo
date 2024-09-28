import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard(client):
    response = client.get('/')
    assert response.status_code == 200  # Check that the page loads successfully
    assert b"Project Dashboard" in response.data  # Verify the title exists
    assert b"CI/CD Pipeline Demo" in response.data  # Verify the project name exists
    assert b"Running" in response.data  # Verify the project status exists
    assert b"v1.0.0" in response.data  # Verify the project version exists
    assert b"srrevis" in response.data  # Verify the project owner exists
