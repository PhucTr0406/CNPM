from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey
from .base_model import Base
import datetime

class DoctorReviewModel(Base):
    __tablename__ = 'DOCTOR_REVIEW'
    review_id = Column(BIGINT, primary_key=True, autoincrement=True)
    analysis_id = Column(BIGINT, ForeignKey('AI_ANALYSIS.analysis_id'))
    
    # Lưu ý: Bạn cần đảm bảo đã có model cho bảng DOCTOR_PROFILE
    # Nếu chưa có, ứng dụng sẽ báo lỗi khi khởi tạo.
    doctor_id = Column(BIGINT, ForeignKey('DOCTOR_PROFILE.doctor_id'))
    
    validation_status = Column(String(20))
    comment = Column(String(1000))
    reviewed_at = Column(DateTime, default=datetime.datetime.utcnow)

class MedicalReportModel(Base):
    __tablename__ = 'MEDICAL_REPORT'
    report_id = Column(BIGINT, primary_key=True, autoincrement=True)
    patient_id = Column(BIGINT, ForeignKey('PATIENT_PROFILE.patient_id'))
    analysis_id = Column(BIGINT, ForeignKey('AI_ANALYSIS.analysis_id'))
    report_url = Column(String(500))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)