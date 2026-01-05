from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base_model import Base
import datetime

class AccountModel(Base):
    __tablename__ = 'ACCOUNT'
    
    account_id = Column(BIGINT, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    
    # role_id nên để Integer hoặc BIGINT tùy theo bảng ROLE bạn thiết kế
    role_id = Column(Integer, ForeignKey('ROLE.role_id'), nullable=True)
    clinic_id = Column(Integer, ForeignKey('CLINIC.clinic_id'), nullable=True)
    
    status = Column(String(50), default='active')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Thêm các mối quan hệ để dễ dàng lấy dữ liệu (Optional)
    # clinic = relationship("ClinicModel", back_populates="accounts")