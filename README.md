# Sales Dashboard Lab - Q4 2026

Welcome to the Sales Dashboard development exercise! You'll build a simple web dashboard to visualize our quarterly sales data.

## Lab Overview

In this lab, you'll create a Flask-based dashboard that displays sales metrics, team performance, and regional data. This is a hands-on exercise to practice working with data visualization and Flask.

**Estimated time:** 45-60 minutes

## Business Context

The sales team needs a simple dashboard to track:
- Monthly revenue trends
- Top performing products
- Regional sales breakdown
- Sales rep performance metrics

Your task is to complete the partially-built dashboard.

## Prerequisites

- Python 3.7 or higher
- Basic understanding of Flask
- Familiarity with data manipulation (helpful but not required)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ThwinHtetWin/api-security-lab.git
cd api-security-lab
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The dashboard should now be running on `http://localhost:5000`

## Lab Exercises

### Exercise 1: Complete Revenue Chart (15 min)

The monthly revenue chart is incomplete. Finish the implementation in `app.py`.

**Task:** Complete the `/api/revenue` endpoint to return monthly data

**Expected Output:** JSON with month and revenue for Q3 2026

### Exercise 2: Add Product Rankings (15 min)

Create an endpoint that returns top 5 products by revenue.

**Task:** Implement `/api/top-products` endpoint

**Data:** Use the sample data in `data/products.csv`

### Exercise 3: Regional Breakdown (15 min)

Display sales by region (North, South, East, West).

**Task:** Complete the `/api/regions` endpoint and add a pie chart to the frontend

### Exercise 4: Sales Rep Leaderboard (15 min)

Show top 10 sales reps by total sales amount.

**Task:** Implement `/api/sales-reps` endpoint

## Verification

Test your endpoints:

```bash
# Test revenue endpoint
curl http://localhost:5000/api/revenue

# Test products endpoint
curl http://localhost:5000/api/top-products

# Run automated tests
pytest tests/
```

## Submission

Once completed:
1. Ensure all endpoints return valid JSON
2. Verify the dashboard displays all charts correctly
3. Run `pytest tests/` - all tests should pass
4. Submit your `app.py` file to the training portal

## Sample Data

Sample sales data is provided in the `data/` directory:
- `sales.csv` - Monthly sales transactions
- `products.csv` - Product catalog
- `reps.csv` - Sales representatives

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Chart.js for visualizations](https://www.chartjs.org/)

## Need Help?

Check `HINTS.md` for guidance or ask the training team.

---
**Developer Training Program - Q4 2026**
