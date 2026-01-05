
from sqlalchemy.orm import relationship

import datetime

from sqlalchemy import Column, Integer, String, Text
from .base_model import Base

class ClinicModel(Base):
    __tablename__ = 'CLINIC'
    clinic_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(500))
    phone = Column(String(20))
    email = Column(String(100))
    website_url = Column(String(255))
    description = Column(Text)