from flask import Blueprint, request, jsonify
from app.core.assessment import HealthRiskAssessment
from app.core.models import load_model

api = Blueprint('api', __name__)

@api.route('/assess', methods=['POST'])
def assess_health():
    """API endpoint for health risk assessment"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['age', 'gender', 'height_cm', 'weight_kg']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Perform assessment
        assessment = HealthRiskAssessment()
        assessment.collect_user_data(data)
        risks = assessment.calculate_risk_scores()
        recommendations = assessment.generate_recommendations(risks)
        action_plan = assessment.generate_action_plan(recommendations)
        
        return jsonify({
            'risks': risks,
            'recommendations': recommendations,
            'action_plan': action_plan
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/predict/<model_type>', methods=['POST'])
def predict(model_type):
    """API endpoint for model predictions"""
    valid_models = ['diabetes', 'heart_disease', 'obesity']
    if model_type not in valid_models:
        return jsonify({'error': 'Invalid model type'}), 400
    
    try:
        model = load_model(model_type)
        if model is None:
            return jsonify({'error': 'Model not available'}), 503
            
        data = request.get_json()
        features = data.get('features', [])
        
        if not features:
            return jsonify({'error': 'No features provided'}), 400
            
        prediction = model.predict([features])[0]
        return jsonify({'prediction': int(prediction)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
