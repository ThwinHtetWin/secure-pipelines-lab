"""
Basic tests for the API Security Lab
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
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'API Security Lab' in response.data

def test_users_endpoint_exists(client):
    """Test that users endpoint exists"""
    response = client.get('/api/users')
    assert response.status_code == 200

def test_user_endpoint_exists(client):
    """Test that user endpoint exists"""
    response = client.get('/api/user/1')
    assert response.status_code == 200
