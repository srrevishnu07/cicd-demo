import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200  # Check if the page loads successfully
    assert b"Project Dashboard" in response.data  # Verify the page title exists

def test_dashboard_project_information(client):
    response = client.get('/')
    assert b"CI/CD Pipeline Demo" in response.data  # Verify project name is correct
    assert b"Running" in response.data  # Verify project status is correct
    assert b"v1.0.0" in response.data  # Verify project version is correct
    assert b"This is a demo project showcasing CI/CD automation" in response.data  # Verify project description exists
    assert b"srrevis" in response.data  # Verify project owner is correct

def test_dashboard_progress_bar(client):
    response = client.get('/')
    assert b"70%" in response.data  # Verify that the progress bar shows 70% completion
    assert b'<div class="progress-bar" style="width: 70%;">70%</div>' in response.data  # Verify progress bar HTML is correct

def test_dashboard_project_statistics(client):
    response = client.get('/')
    assert b"Deployments" in response.data  # Verify the "Deployments" label exists
    assert b"15" in response.data  # Verify the number of deployments is correct
    assert b"Tests Passed" in response.data  # Verify the "Tests Passed" label exists
    assert b"120" in response.data  # Verify the number of tests passed is correct
    assert b"Issues Resolved" in response.data  # Verify the "Issues Resolved" label exists
    assert b"45" in response.data  # Verify the number of issues resolved is correct

def test_dashboard_status_indicator(client):
    response = client.get('/')
    assert b'<span class="status running">Running</span>' in response.data  # Verify "Running" status has the correct class and text
