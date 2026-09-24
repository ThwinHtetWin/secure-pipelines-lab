"""
CI/CD Security Lab - Demo Application
A simple Flask app to demonstrate CI/CD security concepts
"""

from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# VULNERABILITY: Hardcoded secret key (should use environment variable)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'insecure-default-key-change-me')

# Application version and build info
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
BUILD_ID = os.getenv('BUILD_ID', 'local-dev')
DEPLOYED_BY = os.getenv('DEPLOYED_BY', 'unknown')

# Simple HTML template
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Security Lab</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; padding: 20px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .endpoint { background: #fff3cd; padding: 10px; margin: 5px 0; border-left: 3px solid #ffc107; }
        .warning { background: #f8d7da; padding: 15px; border-left: 4px solid #dc3545; margin: 10px 0; }
        .info { background: #d1ecf1; padding: 10px; border-left: 3px solid #0c5460; }
        code { background: #e9ecef; padding: 2px 5px; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔒 CI/CD Security Lab - Demo Application</h1>

        <div class="warning">
            <strong>⚠️ Warning:</strong> This application contains intentional security vulnerabilities for training purposes.
            DO NOT deploy this to production!
        </div>

        <div class="card">
            <h2>Application Info</h2>
            <p><strong>Version:</strong> {{version}}</p>
            <p><strong>Build ID:</strong> {{build_id}}</p>
            <p><strong>Environment:</strong> {{env}}</p>
        </div>

        <div class="card">
            <h2>Your Task</h2>
            <p>Review and fix security vulnerabilities in:</p>
            <div class="info">📄 <code>.github/workflows/ci.yml</code> - GitHub Actions workflow</div>
            <div class="info">🚀 <code>deploy.sh</code> - Deployment script</div>
            <div class="info">🐳 <code>docker-compose.yml</code> - Container configuration</div>
            <div class="info">📦 <code>requirements.txt</code> - Python dependencies</div>
        </div>

        <div class="card">
            <h2>API Endpoints (for testing):</h2>
            <div class="endpoint"><strong>GET /</strong> - This page</div>
            <div class="endpoint"><strong>GET /health</strong> - Health check</div>
            <div class="endpoint"><strong>GET /version</strong> - Version info</div>
            <div class="endpoint"><strong>GET /config</strong> - Configuration (⚠️ Insecure!)</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Main page"""
    return render_template_string(
        HOME_HTML,
        version=APP_VERSION,
        build_id=BUILD_ID,
        env=os.getenv('FLASK_ENV', 'development')
    )

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'cicd-security-lab',
        'version': APP_VERSION
    })

@app.route('/version')
def version():
    """Return version information"""
    return jsonify({
        'version': APP_VERSION,
        'build_id': BUILD_ID,
        'deployed_by': DEPLOYED_BY,
        'python_version': os.sys.version,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/config')
def config():
    """
    VULNERABILITY: This endpoint exposes sensitive configuration!
    Students should identify this as a security issue
    """
    return jsonify({
        'warning': 'This endpoint leaks sensitive information!',
        'secret_key': app.config['SECRET_KEY'],
        'database_url': os.getenv('DATABASE_URL', 'not set'),
        'api_key': os.getenv('API_KEY', 'not set'),
        'debug_mode': app.config.get('DEBUG', False),
        'environment': dict(os.environ)  # Exposing all env vars!
    })

if __name__ == '__main__':
    print("=" * 60)
    print("CI/CD Security Lab - Demo Application")
    print("=" * 60)
    print(f"Version: {APP_VERSION}")
    print(f"Build ID: {BUILD_ID}")
    print("Starting server on http://localhost:5000")
    print("\nEndpoints:")
    print("  - GET /              Home page")
    print("  - GET /health        Health check")
    print("  - GET /version       Version info")
    print("  - GET /config        Config (⚠️ INSECURE!)")
    print("\n⚠️  WARNING: This app contains intentional vulnerabilities!")
    print("=" * 60)

    # VULNERABILITY: Debug mode enabled
    debug_mode = os.getenv('FLASK_DEBUG', '1') == '1'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
