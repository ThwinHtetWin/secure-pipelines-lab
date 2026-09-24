#!/bin/bash

# INSECURE DEPLOYMENT SCRIPT - FOR TRAINING PURPOSES ONLY
# Contains multiple security vulnerabilities

set -e

echo "Starting deployment..."

# VULNERABILITY 1: Hardcoded credentials
DEPLOY_USER="admin"
DEPLOY_PASSWORD="DeployPassword123!"
PRODUCTION_HOST="prod.company.com"

# VULNERABILITY 2: Credentials in environment variables printed to logs
echo "Deploying to $PRODUCTION_HOST as $DEPLOY_USER"

# VULNERABILITY 3: Downloading scripts from the internet without verification
echo "Downloading deployment utilities..."
curl -s https://raw.githubusercontent.com/some-repo/deploy-scripts/main/utils.sh | bash

# VULNERABILITY 4: Using eval with user input
DEPLOY_ENV=${1:-production}
eval "export ENV=$DEPLOY_ENV"

# VULNERABILITY 5: No checksum verification for artifacts
echo "Uploading application artifacts..."
sshpass -p "$DEPLOY_PASSWORD" scp -r dist/* $DEPLOY_USER@$PRODUCTION_HOST:/var/www/app/

# VULNERABILITY 6: Executing remote commands without verification
sshpass -p "$DEPLOY_PASSWORD" ssh $DEPLOY_USER@$PRODUCTION_HOST << 'ENDSSH'
    cd /var/www/app
    # VULNERABILITY 7: Blind execution of uploaded files
    chmod +x *.sh
    ./install.sh

    # VULNERABILITY 8: Restarting services without health checks
    systemctl restart app
ENDSSH

# VULNERABILITY 9: AWS credentials in script
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VULNERABILITY 10: Using aws cli without MFA
aws s3 sync dist/ s3://production-artifacts/

# VULNERABILITY 11: Database password in plaintext
PGPASSWORD="ProdDBPassword123" psql -h db.company.com -U admin -d production -c "UPDATE deployments SET version='$(git rev-parse HEAD)'"

echo "Deployment completed!"

# VULNERABILITY 12: Logging sensitive information
echo "Deployed by: $(whoami) at $(date)" >> /var/log/deployments.log
echo "Credentials used: $DEPLOY_USER:$DEPLOY_PASSWORD" >> /var/log/deployments.log
