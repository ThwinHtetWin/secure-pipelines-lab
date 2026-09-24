"""
Tests for the CI/CD Security Lab Demo Application
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'CI/CD Security Lab' in response.data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'version' in data

def test_version_endpoint(client):
    """Test version endpoint"""
    response = client.get('/version')
    assert response.status_code == 200
    data = response.get_json()
    assert 'version' in data
    assert 'build_id' in data
    assert 'timestamp' in data

def test_config_endpoint_vulnerability(client):
    """Test that config endpoint exposes sensitive data (intentional vulnerability)"""
    response = client.get('/config')
    assert response.status_code == 200
    data = response.get_json()
    # This is intentionally insecure for the lab!
    assert 'secret_key' in data
    assert 'warning' in data
