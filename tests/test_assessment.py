import unittest
from app.core.assessment import HealthRiskAssessment

class TestHealthRiskAssessment(unittest.TestCase):
    def setUp(self):
        self.assessment = HealthRiskAssessment()
        self.sample_data = {
            'age': 45,
            'gender': 'M',
            'height_cm': 175,
            'weight_kg': 80,
            'smoker': False,
            'family_diabetes': True,
            'exercise_frequency': '3-5x/week',
            'diet_quality': 'good'
        }

    def test_bmi_calculation(self):
        self.assessment.collect_user_data({
            'height_cm': 175,
            'weight_kg': 80
        })
        self.assertAlmostEqual(self.assessment.user_data['bmi'], 26.12, places=2)

    def test_diabetes_risk_calculation(self):
        self.assessment.collect_user_data(self.sample_data)
        risk = self.assessment._calculate_diabetes_risk()
        self.assertIn('risk_percent', risk)
        self.assertTrue(0 <= risk['risk_percent'] <= 100)

    def test_heart_disease_risk_calculation(self):
        test_data = {
            **self.sample_data,
            'blood_pressure_systolic': 130,
            'blood_pressure_diastolic': 85,
            'cholesterol_mgdl': 200,
            'hdl_mgdl': 50,
            'family_heart_disease': True
        }
        self.assessment.collect_user_data(test_data)
        risk = self.assessment._calculate_heart_disease_risk()
        self.assertIn('risk_percent', risk)
        self.assertTrue(0 <= risk['risk_percent'] <= 100)

    def test_obesity_risk_calculation(self):
        self.assessment.collect_user_data(self.sample_data)
        risk = self.assessment._calculate_obesity_risk()
        self.assertIn('risk_percent', risk)
        self.assertTrue(0 <= risk['risk_percent'] <= 100)

    def test_recommendation_generation(self):
        self.assessment.collect_user_data(self.sample_data)
        risks = self.assessment.calculate_risk_scores()
        recommendations = self.assessment.generate_recommendations(risks)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()
