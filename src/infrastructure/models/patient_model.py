from sqlalchemy import Column, BIGINT, String, ForeignKey, Date
from .base_model import Base

class PatientProfileModel(Base):
    __tablename__ = 'PATIENT_PROFILE'
    
    patient_id = Column(BIGINT, primary_key=True, autoincrement=True)
    
    # Liên kết với bảng ACCOUNT (đã định nghĩa trong account_model.py)
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    
    date_of_birth = Column(Date)
    gender = Column(String(10))
    medical_history = Column(String(1000))