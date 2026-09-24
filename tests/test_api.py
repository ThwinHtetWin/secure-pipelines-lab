"""
Tests for the Sales Dashboard Lab
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
    """Test the home dashboard page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Sales Dashboard' in response.data

def test_revenue_endpoint(client):
    """Test revenue endpoint returns data"""
    response = client.get('/api/revenue')
    assert response.status_code == 200
    data = response.get_json()
    assert 'success' in data
    assert data['success'] == True
    assert 'data' in data
    assert len(data['data']) > 0

def test_top_products_endpoint(client):
    """Test top products endpoint"""
    response = client.get('/api/top-products')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert len(data['data']) <= 5

def test_regions_endpoint(client):
    """Test regions endpoint"""
    response = client.get('/api/regions')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data

def test_sales_reps_endpoint(client):
    """Test sales reps endpoint"""
    response = client.get('/api/sales-reps')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
