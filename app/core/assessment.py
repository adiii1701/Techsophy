import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import json
from datetime import datetime

class HealthRiskAssessment:
    def __init__(self):
        self.models = {
            'diabetes': None,
            'heart_disease': None,
            'obesity': None
        }
        self.load_models()
        self.user_data = {}
    
    def load_models(self):
        try:
            self.models['diabetes'] = joblib.load('../models/diabetes_model.pkl')
            self.models['heart_disease'] = joblib.load('../models/heart_disease_model.pkl')
            self.models['obesity'] = joblib.load('../models/obesity_model.pkl')
        except Exception as e:
            print(f"Error loading models: {str(e)}")

    def collect_user_data(self, data):
        self.user_data = data
        self._calculate_bmi()
        
    def _calculate_bmi(self):
        if 'height_cm' in self.user_data and 'weight_kg' in self.user_data:
            height_m = self.user_data['height_cm'] / 100
            self.user_data['bmi'] = round(self.user_data['weight_kg'] / (height_m ** 2), 2)
    
    def calculate_risk_scores(self):
        risks = {
            'diabetes': self._calculate_diabetes_risk(),
            'heart_disease': self._calculate_heart_disease_risk(),
            'obesity': self._calculate_obesity_risk(),
            'timestamp': datetime.now().isoformat()
        }
        return risks
    
    def _calculate_diabetes_risk(self):
        score = 0
        if self.user_data['age'] >= 65: score += 10
        elif self.user_data['age'] >= 50: score += 5
        elif self.user_data['age'] >= 40: score += 2
        
        if 'bmi' in self.user_data:
            if self.user_data['bmi'] >= 30: score += 10
            elif self.user_data['bmi'] >= 25: score += 5
        
        if self.user_data.get('family_diabetes', False): score += 10
        if self.user_data.get('exercise_frequency', 'none') in ['none', '1-2x/week']: score += 5
        if self.user_data.get('diet_quality', 'poor') in ['poor', 'fair']: score += 5
        if self.user_data.get('smoker', False): score += 3
        
        risk_percent = min(100, score * 2)
        return {
            'score': score,
            'risk_percent': risk_percent,
            'risk_category': self._get_risk_category(risk_percent)
        }
    
    def _calculate_heart_disease_risk(self):
        score = 0
        if self.user_data.get('gender', 'M') == 'M':
            if self.user_data['age'] >= 55: score += 10
            elif self.user_data['age'] >= 45: score += 5
        else:
            if self.user_data['age'] >= 65: score += 10
            elif self.user_data['age'] >= 55: score += 5
        
        if 'cholesterol_mgdl' in self.user_data and 'hdl_mgdl' in self.user_data:
            if self.user_data['hdl_mgdl'] > 0:
                ratio = self.user_data['cholesterol_mgdl'] / self.user_data['hdl_mgdl']
                if ratio > 5: score += 10
                elif ratio > 4: score += 5
        
        if 'blood_pressure_systolic' in self.user_data and 'blood_pressure_diastolic' in self.user_data:
            if (self.user_data['blood_pressure_systolic'] >= 140 or 
                self.user_data['blood_pressure_diastolic'] >= 90):
                score += 10
            elif (self.user_data['blood_pressure_systolic'] >= 130 or 
                  self.user_data['blood_pressure_diastolic'] >= 85):
                score += 5
        
        if self.user_data.get('family_heart_disease', False): score += 10
        if self.user_data.get('smoker', False): score += 15
        if self.user_data.get('exercise_frequency', 'none') == 'none': score += 5
        
        risk_percent = min(100, score * 1.5)
        return {
            'score': score,
            'risk_percent': risk_percent,
            'risk_category': self._get_risk_category(risk_percent)
        }
    
    def _calculate_obesity_risk(self):
        if 'bmi' not in self.user_data:
            raise ValueError("BMI data missing")
            
        bmi = self.user_data['bmi']
        
        if bmi >= 30:
            status = 'obese'
            risk_percent = 80
        elif bmi >= 25:
            status = 'overweight'
            risk_percent = 50
        else:
            status = 'normal'
            risk_percent = 10
        
        if self.user_data.get('family_obesity', False): risk_percent += 15
        if self.user_data.get('exercise_frequency', 'none') == 'none': risk_percent += 15
        if self.user_data.get('diet_quality', 'poor') == 'poor': risk_percent += 10
        
        risk_percent = min(100, risk_percent)
        return {
            'current_status': status,
            'bmi': bmi,
            'risk_percent': risk_percent,
            'risk_category': self._get_risk_category(risk_percent)
        }
    
    def _get_risk_category(self, percent):
        if percent >= 70: return 'High'
        elif percent >= 40: return 'Moderate'
        else: return 'Low'
    
    def generate_recommendations(self, risks):
        recommendations = []
        
        if self.user_data.get('exercise_frequency', 'none') in ['none', '1-2x/week']:
            recommendations.append({
                'category': 'Exercise',
                'priority': 'High',
                'recommendation': 'Increase physical activity to at least 150 minutes of moderate exercise per week',
                'resources': ['CDC Exercise Guidelines', 'Local gym memberships', 'Fitness apps']
            })
        
        if self.user_data.get('diet_quality', 'poor') in ['poor', 'fair']:
            recommendations.append({
                'category': 'Nutrition',
                'priority': 'High',
                'recommendation': 'Improve diet quality with more fruits, vegetables, and whole grains',
                'resources': ['MyPlate guidelines', 'Nutritionist consultation', 'Healthy recipe websites']
            })
        
        if risks['diabetes']['risk_category'] in ['Moderate', 'High']:
            recommendations.append({
                'category': 'Diabetes Prevention',
                'priority': 'High' if risks['diabetes']['risk_category'] == 'High' else 'Medium',
                'recommendation': 'Monitor blood sugar levels and consider prediabetes screening',
                'resources': ['ADA Diabetes Risk Test', 'Blood glucose monitoring devices']
            })
        
        if risks['heart_disease']['risk_category'] in ['Moderate', 'High']:
            recommendations.append({
                'category': 'Heart Health',
                'priority': 'High' if risks['heart_disease']['risk_category'] == 'High' else 'Medium',
                'recommendation': 'Get regular cholesterol and blood pressure checks',
                'resources': ['AHA Heart Health Guidelines', 'Cardiologist consultation']
            })
        
        if risks['obesity']['risk_category'] in ['Moderate', 'High']:
            recommendations.append({
                'category': 'Weight Management',
                'priority': 'High' if risks['obesity']['risk_category'] == 'High' else 'Medium',
                'recommendation': 'Develop a weight management plan with diet and exercise',
                'resources': ['BMI calculator', 'Weight loss programs', 'Dietitian consultation']
            })
        
        if self.user_data.get('smoker', False):
            recommendations.append({
                'category': 'Smoking',
                'priority': 'High',
                'recommendation': 'Quit smoking to reduce multiple health risks',
                'resources': ['Smoking cessation programs', 'Nicotine replacement therapies']
            })
        
        return recommendations
    
    def generate_action_plan(self, recommendations):
        action_plan = {
            'short_term_goals': [],
            'long_term_goals': [],
            'follow_up_schedule': []
        }
        
        for rec in recommendations:
            if rec['priority'] == 'High':
                action_plan['short_term_goals'].append({
                    'goal': rec['recommendation'],
                    'timeline': '1-2 weeks',
                    'resources': rec['resources']
                })
            else:
                action_plan['long_term_goals'].append({
                    'goal': rec['recommendation'],
                    'timeline': '3-6 months',
                    'resources': rec['resources']
                })
        
        action_plan['follow_up_schedule'].append({
            'action': 'Reassess health metrics',
            'timeline': '3 months',
            'purpose': 'Track progress and adjust recommendations'
        })
        
        return action_plan
    
    def save_results(self, risks, recommendations, action_plan, filename='health_assessment.json'):
        results = {
            'user_data': self.user_data,
            'risk_assessment': risks,
            'recommendations': recommendations,
            'action_plan': action_plan,
            'timestamp': datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
