# Insecure CI/CD Pipeline Lab - October 2026

Welcome to the CI/CD Security hands-on lab! You'll identify and fix common security vulnerabilities in CI/CD pipelines.

## Lab Overview

In this lab, you'll work with a sample application that has an **insecure GitHub Actions CI/CD pipeline**. Your task is to identify security vulnerabilities in the pipeline configuration and fix them.

**Estimated time:** 60-90 minutes

## Business Context

Modern DevOps practices rely heavily on CI/CD pipelines, but they often introduce security risks:
- Exposed secrets and credentials
- Overly permissive permissions
- Unverified third-party actions
- Lack of security scanning
- Insecure artifact handling

Your task is to secure our CI/CD pipeline following industry best practices.

## Prerequisites

- Python 3.7 or higher
- Basic understanding of CI/CD concepts
- Familiarity with GitHub Actions (helpful but not required)
- Understanding of security principles

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ThwinHtetWin/secure-pipelines-lab.git
cd secure-pipelines-lab
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

### Exercise 1: Secrets Management (20 min)

The GitHub Actions workflow in `.github/workflows/ci.yml` has hardcoded secrets.

**Vulnerabilities:**
- Hardcoded API keys in workflow file
- Database credentials committed to repo
- AWS credentials exposed

**Task:** Identify all hardcoded secrets and implement proper secret management

### Exercise 2: Dependency Security (20 min)

The CI pipeline doesn't scan for vulnerable dependencies.

**Task:**
- Add dependency scanning (pip-audit, safety, or similar)
- Configure vulnerability reporting
- Set up automated dependency updates

### Exercise 3: Permission Hardening (15 min)

The workflow uses overly permissive GitHub token permissions.

**Task:**
- Review `permissions:` in workflow
- Apply principle of least privilege
- Document why each permission is needed

### Exercise 4: Supply Chain Security (20 min)

The pipeline uses third-party GitHub Actions without verification.

**Task:**
- Pin action versions to specific commit SHAs
- Verify action sources
- Add checksum verification for dependencies

### Exercise 5: Secure Artifact Handling (15 min)

Build artifacts are uploaded without security controls.

**Task:**
- Add artifact signing
- Implement integrity checks
- Configure retention policies

## Verification

Test the application:

```bash
# Run the Flask app
python app.py

# Run security checks (add these to CI!)
pip-audit
bandit -r .
pytest tests/

# Validate your CI/CD fixes
cat .github/workflows/ci.yml  # Review your changes
```

## Submission

Once completed:
1. All secrets removed from code and configs
2. Security scanning added to CI pipeline
3. Workflow permissions follow least privilege
4. All third-party actions pinned and verified
5. Submit your fixed `.github/workflows/ci.yml` file

## Vulnerable Files to Review

- `.github/workflows/ci.yml` - **Main focus**: Insecure CI/CD pipeline
- `.env.example` - Check for accidentally committed secrets
- `requirements.txt` - Review for known vulnerabilities
- `deploy.sh` - Insecure deployment script
- `docker-compose.yml` - Container security issues

## Resources

- [GitHub Actions Security Hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [OWASP CI/CD Security Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
- [Supply Chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)
- [OpenSSF Scorecard](https://github.com/ossf/scorecard)

## Need Help?

Check `HINTS.md` for guidance or ask the security training team.

## Bonus Challenges

If you finish early:
- Add SAST scanning with CodeQL
- Implement signed commits verification
- Add container image scanning
- Set up SBOM generation
- Configure branch protection rules

---
**Security Training Initiative - October 2026**
