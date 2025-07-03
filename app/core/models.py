from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
import numpy as np

def train_diabetes_model():
    """Train and save diabetes risk prediction model"""
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_classes=2,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Diabetes model accuracy: {acc:.2f}")
    
    joblib.dump(model, '../models/diabetes_model.pkl')

def train_heart_disease_model():
    """Train and save heart disease risk prediction model"""
    X, y = make_classification(
        n_samples=1200,
        n_features=12,
        n_classes=2,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=7,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Heart disease model accuracy: {acc:.2f}")
    
    joblib.dump(model, '../models/heart_disease_model.pkl')

def train_obesity_model():
    """Train and save obesity risk prediction model"""
    X, y = make_classification(
        n_samples=800,
        n_features=8,
        n_classes=3,
        random_state=42
    )
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Obesity model accuracy: {acc:.2f}")
    
    joblib.dump(model, '../models/obesity_model.pkl')

def load_model(model_type):
    """Load a pre-trained model"""
    model_path = f'../models/{model_type}_model.pkl'
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        print(f"Model file not found: {model_path}")
        return None
