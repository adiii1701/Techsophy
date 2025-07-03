import unittest
from app import create_app
from app.core.models import train_diabetes_model

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        train_diabetes_model()

    def test_assess_endpoint(self):
        test_data = {
            'age': 45,
            'gender': 'M',
            'height_cm': 175,
            'weight_kg': 80,
            'smoker': False
        }
        
        response = self.client.post('/api/assess', json=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('risks', response.json)
        self.assertIn('recommendations', response.json)

    def test_predict_endpoint(self):
        test_features = [45, 1, 175, 80, 0, 200, 50, 130, 85, 0]
        
        response = self.client.post('/api/predict/diabetes', json={
            'features': test_features
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json)

    def test_invalid_model_type(self):
        response = self.client.post('/api/predict/invalid_model', json={
            'features': [1, 2, 3]
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
