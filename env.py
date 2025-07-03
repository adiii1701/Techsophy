#######################################
# HEALTH RISK ASSESSMENT TOOL CONFIG
#######################################

# ================
# CORE SETTINGS
# ================

# Flask secret key (generate a new one for production)
SECRET_KEY=your-unique-secret-key-12345

# Debug mode (True for development, False in production)
DEBUG=True

# Server host (0.0.0.0 for Docker, 127.0.0.1 for local)
HOST=0.0.0.0

# Server port
PORT=5000

# ================
# DATABASE CONFIG
# ================

# SQLite (default for development)
DATABASE_URI=sqlite:///health_assessments.db

# PostgreSQL example:
# DATABASE_URI=postgresql://username:password@localhost:5432/healthdb

# MySQL example:
# DATABASE_URI=mysql+pymysql://username:password@localhost:3306/healthdb

# ================
# MODEL PATHS
# ================

# Path to store trained ML models
MODEL_PATH=./models/

# ================
# API SECURITY
# ================

# Comma-separated allowed origins (for CORS)
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# API rate limiting (requests per minute)
API_RATE_LIMIT=100

# ================
# FEATURE TOGGLES
# ================

# Enable/disable registration
ALLOW_REGISTRATION=True

# Enable/disable email verification
REQUIRE_EMAIL_VERIFICATION=False

# ================
# EMAIL CONFIG
# ================

# SMTP Server Configuration
# SMTP_SERVER=smtp.example.com
# SMTP_PORT=587
# SMTP_USE_TLS=True
# SMTP_USERNAME=your@email.com
# SMTP_PASSWORD=your-email-password
# EMAIL_FROM=noreply@yourdomain.com

# ================
# LOGGING CONFIG
# ================

# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Log file path
LOG_FILE=./logs/health_assessment.log

#######################################
# END OF CONFIGURATION
#######################################