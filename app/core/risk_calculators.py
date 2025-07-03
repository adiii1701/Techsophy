def calculate_diabetes_risk(user_data):
    """Calculate diabetes risk score (0-100)"""
    score = 0
    if user_data['age'] >= 65: score += 10
    elif user_data['age'] >= 50: score += 5
    elif user_data['age'] >= 40: score += 2
    
    if 'bmi' in user_data:
        if user_data['bmi'] >= 30: score += 10
        elif user_data['bmi'] >= 25: score += 5
    
    if user_data.get('family_diabetes', False): score += 10
    if user_data.get('exercise_frequency', 'none') in ['none', '1-2x/week']: score += 5
    if user_data.get('diet_quality', 'poor') in ['poor', 'fair']: score += 5
    if user_data.get('smoker', False): score += 3
    
    return min(100, score * 2)

def calculate_heart_disease_risk(user_data):
    """Calculate heart disease risk score (0-100)"""
    score = 0
    if user_data.get('gender', 'M') == 'M':
        if user_data['age'] >= 55: score += 10
        elif user_data['age'] >= 45: score += 5
    else:
        if user_data['age'] >= 65: score += 10
        elif user_data['age'] >= 55: score += 5
    
    if 'cholesterol_mgdl' in user_data and 'hdl_mgdl' in user_data:
        if user_data['hdl_mgdl'] > 0:
            ratio = user_data['cholesterol_mgdl'] / user_data['hdl_mgdl']
            if ratio > 5: score += 10
            elif ratio > 4: score += 5
    
    if 'blood_pressure_systolic' in user_data and 'blood_pressure_diastolic' in user_data:
        if (user_data['blood_pressure_systolic'] >= 140 or 
            user_data['blood_pressure_diastolic'] >= 90):
            score += 10
        elif (user_data['blood_pressure_systolic'] >= 130 or 
              user_data['blood_pressure_diastolic'] >= 85):
            score += 5
    
    if user_data.get('family_heart_disease', False): score += 10
    if user_data.get('smoker', False): score += 15
    if user_data.get('exercise_frequency', 'none') == 'none': score += 5
    
    return min(100, score * 1.5)

def calculate_obesity_risk(user_data):
    """Calculate obesity risk score (0-100)"""
    if 'bmi' not in user_data:
        raise ValueError("BMI data missing")
        
    bmi = user_data['bmi']
    
    if bmi >= 30:
        risk_percent = 80
    elif bmi >= 25:
        risk_percent = 50
    else:
        risk_percent = 10
    
    if user_data.get('family_obesity', False): risk_percent += 15
    if user_data.get('exercise_frequency', 'none') == 'none': risk_percent += 15
    if user_data.get('diet_quality', 'poor') == 'poor': risk_percent += 10
    
    return min(100, risk_percent)

def get_risk_category(risk_percent):
    """Convert risk percentage to category"""
    if risk_percent >= 70: return 'High'
    elif risk_percent >= 40: return 'Moderate'
    else: return 'Low'
