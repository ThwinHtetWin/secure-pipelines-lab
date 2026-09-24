# Hints for CI/CD Security Lab

## Exercise 1: Secrets Management

**Vulnerabilities to find in `.github/workflows/ci.yml`:**
- Line 20: `permissions: write-all` (too permissive)
- Lines 32-35: Hardcoded DATABASE_URL, API_KEY, AWS credentials
- Line 44: API key echoed to logs
- Line 59: DEPLOY_TOKEN and SSH_KEY hardcoded

**Solutions:**
```yaml
# Use GitHub Secrets instead
env:
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
  API_KEY: ${{ secrets.API_KEY }}

# Use OIDC for AWS instead of access keys
permissions:
  id-token: write
  contents: read
```

**Also check:**
- `deploy.sh` - Multiple hardcoded credentials throughout
- `.env.example` - Commented old credentials (should be removed)

## Exercise 2: Dependency Security

**Add to workflow:**
```yaml
- name: Security scan dependencies
  run: |
    pip install pip-audit safety
    pip-audit --desc
    safety check --json
```

**Tools to consider:**
- `pip-audit` - Official PyPA tool
- `safety` - Check against vulnerability database
- `bandit` - Python security linter
- Dependabot - Automated updates

## Exercise 3: Permission Hardening

**Current (insecure):**
```yaml
permissions: write-all
```

**Fixed (least privilege):**
```yaml
permissions:
  contents: read      # Read repo
  pull-requests: write # Comment on PRs
  issues: write       # Create issues
  id-token: write     # For OIDC
```

**Principle:** Only grant permissions actually needed by the workflow.

## Exercise 4: Supply Chain Security

**Vulnerable:**
```yaml
uses: actions/checkout@v4
uses: actions/setup-python@v4
uses: some-random-org/slack-notify@master
```

**Secure (pinned to commit SHA):**
```yaml
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11  # v4.1.1
uses: actions/setup-python@65d7f2d534ac1bc67fcd62888c5f4f3d2cb2b236  # v4.7.1
# Remove untrusted third-party actions
```

**Verification:**
- Check action source on GitHub
- Review the commit SHA
- Use only verified/official actions when possible

## Exercise 5: Secure Artifact Handling

**Issues in workflow:**
- No retention policy (line 57)
- No integrity verification
- No artifact signing

**Solutions:**
```yaml
- name: Upload artifacts
  uses: actions/upload-artifact@v3
  with:
    name: dist
    path: dist/
    retention-days: 7  # Not 90!
    if-no-files-found: error

- name: Generate checksum
  run: sha256sum dist/* > checksums.txt

- name: Sign artifacts
  run: |
    # Use cosign or similar
    cosign sign-blob --key key.pem dist/package.whl
```

## Docker Compose Issues

**In `docker-compose.yml`:**

1. **Secrets in plaintext** (lines 11-16): Use Docker secrets or .env files
2. **Running as root** (line 29): Add `user: "1000:1000"`
3. **Privileged mode** (line 36): Remove unless absolutely necessary
4. **No resource limits**: Add memory/CPU limits
5. **Using :latest tag** (line 42): Pin to specific versions
6. **Database exposed** (line 51): Remove port mapping if not needed

## Deployment Script Issues

**In `deploy.sh`:**

1. **Lines 8-10**: Hardcoded credentials
2. **Line 21**: Downloading random scripts from internet
3. **Line 25**: Using `eval` with variables
4. **Line 29**: Using `sshpass` (stores password in process list)
5. **Lines 41-42**: AWS credentials in script
6. **Line 51**: Logging sensitive data

**Solutions:**
- Use SSH keys instead of passwords
- Use AWS IAM roles instead of access keys
- Never log credentials
- Validate all inputs
- Use secure credential stores (e.g., Hashicorp Vault)

## Quick Wins

### 1. Scan for secrets already committed:
```bash
git log -p | grep -i "password\|secret\|key" | head -20
```

### 2. Add pre-commit hooks:
```bash
pip install detect-secrets
detect-secrets scan > .secrets.baseline
```

### 3. Use environment-specific configs:
```bash
# Don't: Hardcode in files
# Do: Use environment variables
DATABASE_URL=${DATABASE_URL:-"postgresql://localhost/dev"}
```

## Resources

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [OWASP CI/CD Top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
- [Sigstore/Cosign](https://docs.sigstore.dev/) for artifact signing
- [SLSA Framework](https://slsa.dev/) for supply chain security
