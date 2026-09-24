"""
Sales Dashboard Lab - Q4 2026
A simple Flask dashboard for visualizing sales data
"""

from flask import Flask, jsonify, render_template_string
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sales-dashboard-2026'

# Sample data (in production, this would come from a database)
SAMPLE_REVENUE = [
    {'month': 'July', 'revenue': 125000},
    {'month': 'August', 'revenue': 142000},
    {'month': 'September', 'revenue': 138000},
]

SAMPLE_PRODUCTS = [
    {'name': 'Enterprise License', 'revenue': 250000, 'units': 50},
    {'name': 'Professional License', 'revenue': 180000, 'units': 120},
    {'name': 'Starter License', 'revenue': 95000, 'units': 380},
    {'name': 'Support Package', 'revenue': 75000, 'units': 150},
    {'name': 'Training Services', 'revenue': 45000, 'units': 30},
]

SAMPLE_REGIONS = [
    {'region': 'North', 'revenue': 185000},
    {'region': 'South', 'revenue': 142000},
    {'region': 'East', 'revenue': 203000},
    {'region': 'West', 'revenue': 115000},
]

SAMPLE_REPS = [
    {'name': 'Alice Johnson', 'sales': 95000, 'deals': 12},
    {'name': 'Bob Smith', 'sales': 87000, 'deals': 15},
    {'name': 'Carol Davis', 'sales': 82000, 'deals': 10},
    {'name': 'David Wilson', 'sales': 78000, 'deals': 14},
    {'name': 'Emma Brown', 'sales': 71000, 'deals': 11},
]

# Simple HTML template for the dashboard
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sales Dashboard - Q4 2026</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; padding: 20px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .endpoint { background: #e8f5e9; padding: 10px; margin: 5px 0; border-left: 3px solid #4caf50; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Sales Dashboard Lab</h1>
        <div class="card">
            <h2>Welcome!</h2>
            <p>This is the Sales Dashboard training exercise. Complete the API endpoints to power the dashboard.</p>
        </div>
        <div class="card">
            <h2>Available Endpoints:</h2>
            <div class="endpoint"><strong>GET /api/revenue</strong> - Monthly revenue data</div>
            <div class="endpoint"><strong>GET /api/top-products</strong> - Top 5 products by revenue</div>
            <div class="endpoint"><strong>GET /api/regions</strong> - Sales by region</div>
            <div class="endpoint"><strong>GET /api/sales-reps</strong> - Top sales representatives</div>
        </div>
        <div class="card">
            <h3>Quick Test:</h3>
            <p>Test your endpoints with: <code>curl http://localhost:5000/api/revenue</code></p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Main dashboard page"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/revenue')
def get_revenue():
    """
    TODO: Exercise 1 - Return monthly revenue data for Q3 2026
    This is partially complete. Students should verify it returns correct data.
    """
    return jsonify({
        'success': True,
        'data': SAMPLE_REVENUE,
        'period': 'Q3 2026'
    })

@app.route('/api/top-products')
def get_top_products():
    """
    TODO: Exercise 2 - Return top 5 products by revenue
    Students need to implement this endpoint
    """
    # Sort products by revenue and return top 5
    sorted_products = sorted(SAMPLE_PRODUCTS, key=lambda x: x['revenue'], reverse=True)[:5]
    return jsonify({
        'success': True,
        'data': sorted_products
    })

@app.route('/api/regions')
def get_regions():
    """
    TODO: Exercise 3 - Return sales breakdown by region
    Students should complete this endpoint
    """
    return jsonify({
        'success': True,
        'data': SAMPLE_REGIONS
    })

@app.route('/api/sales-reps')
def get_sales_reps():
    """
    TODO: Exercise 4 - Return top 10 sales reps
    Students should implement ranking logic
    """
    sorted_reps = sorted(SAMPLE_REPS, key=lambda x: x['sales'], reverse=True)[:10]
    return jsonify({
        'success': True,
        'data': sorted_reps
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'sales-dashboard'})

if __name__ == '__main__':
    print("=" * 50)
    print("Sales Dashboard Lab - Q4 2026")
    print("=" * 50)
    print("Starting server on http://localhost:5000")
    print("\nEndpoints:")
    print("  - GET /              Dashboard home")
    print("  - GET /api/revenue   Monthly revenue")
    print("  - GET /api/top-products  Top products")
    print("  - GET /api/regions   Regional breakdown")
    print("  - GET /api/sales-reps    Sales leaderboard")
    print("=" * 50)
    app.run(debug=True, port=5000)
