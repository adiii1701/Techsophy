# Health Risk Assessment Tool

*A personalized health risk evaluation system* 


The Health Risk Assessment Tool is a user-friendly web application designed to evaluate an individual's risk of developing chronic health conditions such as Diabetes, Heart Disease, and Obesity. By analyzing user-provided health metrics through pre-trained machine learning models, the tool offers personalized risk scores, visual reports, and actionable lifestyle recommendations.

Whether you're a healthcare provider, researcher, or simply someone looking to monitor and improve your well-being, this tool provides a convenient way to assess health risks and promote proactive care.

## Features

- 🩺 **Comprehensive Risk Assessment**  
  Diabetes | Heart Disease | Obesity
- 📊 **Personalized Reports**  
  Detailed risk scores and trends
- 💡 **Actionable Recommendations**  
  Customized health improvement plans
- 🔒 **Secure Data Storage**  
  Encrypted user data protection
- 🌐 **REST API**  
  Easy integration with other systems

## Installation

### Prerequisites
- Python 3.9+
- pip package manager
- SQLite (default) or PostgreSQL

### Steps
```bash
# Clone repository
git clone https://github.com/yourusername/health-risk-assessment-tool.git
cd health-risk-assessment-tool

# Install dependencies
pip install -r requirements.txt

# Train ML models
python -c "from app.core.models import train_diabetes_model, train_heart_disease_model, train_obesity_model; train_diabetes_model(); train_heart_disease_model(); train_obesity_model()"

# Configure environment (copy example)
cp .env.example .env  # Then edit .env file

# Run application
python run.py
```

## API Documentation

### Base URL
```
http://localhost:5000/api/v1
```

### Endpoints

| Endpoint         | Method | Description                        |
|------------------|--------|------------------------------------|
| /assess          | POST   | Submit health data for assessment |
| /predict/{model} | POST   | Get specific model prediction     |

### Sample Request
```json
{
  "age": 45,
  "gender": "M",
  "height_cm": 175,
  "weight_kg": 80
}
```

## Development Setup

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### Install dev dependencies
```bash
pip install -r requirements-dev.txt
```

### Run tests
```bash
python -m pytest tests/
```

## Deployment

### Docker
```bash
docker build -t health-assessment .
docker run -p 5000:5000 health-assessment
```

### Production Checklist
- [ ] Set DEBUG=False in .env
- [ ] Configure production database
- [ ] Set up HTTPS
- [ ] Implement backup system
