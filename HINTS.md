# Hints for API Security Lab

## Exercise 1: SQL Injection

**Hint 1:** Try sending a username parameter with a single quote: `?username='`

**Hint 2:** Use parameterized queries instead of string concatenation

**Solution:** Replace the vulnerable query with:
```python
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

## Exercise 2: Authentication Bypass

**Hint 1:** The token is hardcoded and easy to guess

**Hint 2:** Consider using Flask-Login or JWT tokens

**Solution:** Implement proper session-based authentication or JWT

## Exercise 3: IDOR

**Hint 1:** Any user can access any other user's data by changing the ID

**Hint 2:** Add authorization checks to verify the logged-in user can access this resource

**Solution:** Verify user identity before returning sensitive data

## Exercise 4: Rate Limiting

**Hint 1:** Use Flask-Limiter extension

**Hint 2:** Apply limits like `@limiter.limit("5 per minute")`

**Solution:**
```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)
```
