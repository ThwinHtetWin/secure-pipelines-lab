# API Security Lab - October 2026

Welcome to the API Security hands-on lab! This exercise will help you understand common API security vulnerabilities and how to fix them.

## Lab Overview

In this lab, you'll work with a simple Flask API that has several security vulnerabilities. Your task is to identify and fix them.

**Estimated time:** 45-60 minutes

## Prerequisites

- Python 3.7 or higher
- Basic understanding of REST APIs
- Familiarity with Flask (helpful but not required)

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

The API should now be running on `http://localhost:5000`

## Lab Exercises

### Exercise 1: SQL Injection (15 min)

Test the `/api/users` endpoint for SQL injection vulnerabilities.

**Task:** Fix the vulnerable query in `app.py`

### Exercise 2: Authentication Bypass (15 min)

The `/api/admin` endpoint has weak authentication. Can you bypass it?

**Task:** Implement proper authentication

### Exercise 3: IDOR (Insecure Direct Object Reference) (15 min)

Check if users can access other users' data at `/api/user/<id>`

**Task:** Add proper authorization checks

### Exercise 4: Rate Limiting (10 min)

The API has no rate limiting. Add it to prevent abuse.

**Task:** Implement rate limiting for sensitive endpoints

## Verification

Run the test suite to verify your fixes:

```bash
pytest tests/
```

## Submission

Once you've completed all exercises and all tests pass, submit your fixed `app.py` file.

## Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/3.0.x/security/)

## Need Help?

Contact the training team or check the hints in `HINTS.md`

---
**Security Training Initiative - October 2026**
