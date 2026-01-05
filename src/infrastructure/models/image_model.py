from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Integer
from .base_model import Base
import datetime

class RetinalImageModel(Base):
    __tablename__ = 'RETINAL_IMAGE'
    
    image_id = Column(BIGINT, primary_key=True, autoincrement=True)
    
    # Đảm bảo bảng PATIENT_PROFILE và CLINIC đã được định nghĩa
    patient_id = Column(BIGINT, ForeignKey('PATIENT_PROFILE.patient_id'))
    clinic_id = Column(Integer, ForeignKey('CLINIC.clinic_id'))
    
    image_url = Column(String(500), nullable=False)
    image_type = Column(String(20))  # Ví dụ: Left Eye, Right Eye
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)