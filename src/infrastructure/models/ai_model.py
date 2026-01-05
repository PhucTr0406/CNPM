from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Integer, Numeric, Text
from .base_model import Base
import datetime

class AIAnalysisModel(Base):
    __tablename__ = 'AI_ANALYSIS'
    analysis_id = Column(BIGINT, primary_key=True, autoincrement=True)
    image_id = Column(BIGINT, ForeignKey('RETINAL_IMAGE.image_id'))
    ai_model_version_id = Column(Integer, ForeignKey('AI_MODEL_VERSION.ai_model_version_id'))
    analysis_time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(20))

class AIResultModel(Base):
    __tablename__ = 'AI_RESULT'
    result_id = Column(BIGINT, primary_key=True, autoincrement=True)
    analysis_id = Column(BIGINT, ForeignKey('AI_ANALYSIS.analysis_id'))
    disease_type = Column(String(100))
    # Numeric(5,2) phù hợp cho giá trị như 99.99
    confidence_score = Column(Numeric(5, 2)) 
    risk_level = Column(String(20))

class AIAnnotationModel(Base):
    __tablename__ = 'AI_ANNOTATION'
    annotation_id = Column(BIGINT, primary_key=True, autoincrement=True)
    analysis_id = Column(BIGINT, ForeignKey('AI_ANALYSIS.analysis_id'))
    coordinates = Column(Text)  # Lưu tọa độ vùng tổn thương (JSON string)
    label = Column(String(100))