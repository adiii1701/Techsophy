import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Application settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///health_assessments.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Model paths
    MODEL_PATH = os.getenv('MODEL_PATH', '../models/')
    
    # API settings
    API_PREFIX = '/api/v1'
    API_TITLE = 'Health Risk Assessment API'
    API_VERSION = '1.0'
    OPENAPI_VERSION = '3.0.2'
    
    # CORS settings
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '').split(',')
