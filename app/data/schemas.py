from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserAssessment(Base):
    """Database model for storing health assessments"""
    __tablename__ = 'user_assessments'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    assessment_data = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(DateTime, server_default='CURRENT_TIMESTAMP', 
                       server_onupdate='CURRENT_TIMESTAMP')

def init_db(db_uri):
    """Initialize database connection and create tables"""
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

def save_assessment(db_session, user_id, assessment_data):
    """Save assessment to database"""
    session = db_session()
    try:
        assessment = UserAssessment(
            user_id=user_id,
            assessment_data=assessment_data
        )
        session.add(assessment)
        session.commit()
        return assessment.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_assessments(db_session, user_id):
    """Retrieve assessments for a user"""
    session = db_session()
    try:
        return session.query(UserAssessment)\
            .filter(UserAssessment.user_id == user_id)\
            .order_by(UserAssessment.created_at.desc())\
            .all()
    finally:
        session.close()
