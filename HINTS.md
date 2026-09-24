# Hints for Sales Dashboard Lab

## Exercise 1: Revenue Endpoint

**Hint 1:** The endpoint is already implemented! Just verify it works.

**Test it:**
```bash
curl http://localhost:5000/api/revenue
```

**Expected output:** JSON with monthly revenue for July, August, September 2026

## Exercise 2: Top Products

**Hint 1:** The products are already in the `SAMPLE_PRODUCTS` list

**Hint 2:** Sort by the 'revenue' field in descending order

**Solution approach:**
```python
sorted_products = sorted(SAMPLE_PRODUCTS, key=lambda x: x['revenue'], reverse=True)[:5]
```

## Exercise 3: Regional Breakdown

**Hint 1:** The data is in `SAMPLE_REGIONS` list

**Hint 2:** Return the data as JSON with proper structure

**Test it:**
```bash
curl http://localhost:5000/api/regions
```

## Exercise 4: Sales Rep Leaderboard

**Hint 1:** Sort by the 'sales' field to rank representatives

**Hint 2:** Return top 10, even though sample data has only 5

**Solution approach:**
```python
sorted_reps = sorted(SAMPLE_REPS, key=lambda x: x['sales'], reverse=True)[:10]
```

## Bonus: Add More Features

If you finish early, try adding:
- Filter revenue by specific month
- Search products by name
- Add pagination to results
- Calculate total revenue across all regions
