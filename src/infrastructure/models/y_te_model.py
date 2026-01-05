from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Integer, Boolean, Date, Numeric
from infrastructure.databases.base import Base
from sqlalchemy.orm import relationship
import datetime

class AccountModel(Base):
    __tablename__ = 'ACCOUNT'
    account_id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('ROLE.role_id'))
    clinic_id = Column(Integer, ForeignKey('CLINIC.clinic_id'), nullable=True)
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class PatientProfileModel(Base):
    __tablename__ = 'PATIENT_PROFILE'
    patient_id = Column(BIGINT, primary_key=True, autoincrement=True) # Thêm autoincrement
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    date_of_birth = Column(Date)
    gender = Column(String(10))
    medical_history = Column(String(1000))

class RetinalImageModel(Base):
    __tablename__ = 'RETINAL_IMAGE'
    image_id = Column(BIGINT, primary_key=True, autoincrement=True) # Thêm autoincrement
    patient_id = Column(BIGINT, ForeignKey('PATIENT_PROFILE.patient_id'))
    clinic_id = Column(Integer, ForeignKey('CLINIC.clinic_id'))
    image_url = Column(String(500))
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)