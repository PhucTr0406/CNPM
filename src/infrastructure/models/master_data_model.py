from sqlalchemy import Column, BIGINT, String, ForeignKey, Integer
from .base_model import Base

class RoleModel(Base):
    __tablename__ = 'ROLE'
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), unique=True)

class ServicePackageModel(Base):
    __tablename__ = 'SERVICE_PACKAGE'
    package_id = Column(Integer, primary_key=True, autoincrement=True)
    package_name = Column(String(100))
    price = Column(BIGINT)

class AIModelVersionModel(Base):
    __tablename__ = 'AI_MODEL_VERSION'
    ai_model_version_id = Column(Integer, primary_key=True, autoincrement=True)
    version_name = Column(String(50))

class DoctorProfileModel(Base): # <--- Đảm bảo tên Class đúng từng chữ cái này
    __tablename__ = 'DOCTOR_PROFILE'
    doctor_id = Column(BIGINT, primary_key=True, autoincrement=True)
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    specialization = Column(String(255))
    experience_years = Column(Integer)