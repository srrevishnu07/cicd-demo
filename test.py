import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_project_dashboard(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["project_name"] == "CI/CD Pipeline Demo"
    assert json_data["status"] == "Running"
    assert json_data["version"] == "v1.0.0"
    assert "description" in json_data
    assert json_data["owner"] == "srrevis"
