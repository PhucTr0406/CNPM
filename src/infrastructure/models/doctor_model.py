from sqlalchemy import Column, BIGINT, String, ForeignKey
from .base_model import Base

class DoctorProfileModel(Base):
    __tablename__ = 'DOCTOR_PROFILE'
    doctor_id = Column(BIGINT, primary_key=True, autoincrement=True)
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    specialization = Column(String(255))
    license_number = Column(String(50))