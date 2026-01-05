from .base import Base
from .session import engine

# 1. IMPORT CÁC MODEL THEO THỨ TỰ LOGIC (Cha trước - Con sau để tránh lỗi Metadata)
try:
    # --- Tầng 1: Master Data & Account (Các bảng độc lập hoặc làm gốc) ---
    from infrastructure.models.master_data_model import (
        RoleModel, 
        ServicePackageModel, 
        AIModelVersionModel, 
        DoctorProfileModel
    )
    from infrastructure.models.account_model import AccountModel
    from infrastructure.models.clinic_model import ClinicModel

    # --- Tầng 2: Profiles & Core (Phụ thuộc vào Account/Clinic) ---
    from infrastructure.models.patient_model import PatientProfileModel
    from infrastructure.models.notification_model import NotificationModel
    from infrastructure.models.billing_model import SubscriptionModel, PaymentModel

    # --- Tầng 3: Medical Data (Phụ thuộc vào Patient/Doctor) ---
    from infrastructure.models.image_model import RetinalImageModel
    from infrastructure.models.chat_model import ConversationModel, MessageModel
    from infrastructure.models.report_model import DoctorReviewModel, MedicalReportModel

    # --- Tầng 4: AI Results (Phụ thuộc vào Image/AI Model Version) ---
    from infrastructure.models.ai_model import (
        AIAnalysisModel, 
        AIResultModel, 
        AIAnnotationModel
    )

    print(">>> [SUCCESS]: Tất cả Model đã được nạp vào hệ thống.")

except ImportError as e:
    print(f">>> [ERROR]: Lỗi Import Model. Kiểm tra tên Class hoặc tên File: {e}")

# 2. HÀM KHỞI TẠO CẤU TRÚC BẢNG
def init_models():
    """
    Quét toàn bộ Metadata và thực thi lệnh CREATE TABLE trên SQL Server.
    """
    try:
        print(">>> SQLALCHEMY: Đang kiểm tra và tạo các bảng còn thiếu...")
        # Lệnh này sẽ tự động bỏ qua các bảng đã tồn tại
        Base.metadata.create_all(bind=engine)
        print(">>> [DATABASE]: Khởi tạo cấu trúc bảng thành công!")
    except Exception as e:
        # Lỗi thường gặp ở đây là Foreign Key trỏ đến bảng chưa được nạp (như DoctorProfile)
        print(f">>> [DATABASE ERROR]: Không thể tạo bảng. Chi tiết: {e}")

# 3. HÀM TÍCH HỢP VỚI FLASK
def init_db(app):
    """
    Kết nối vào vòng đời của Flask App.
    """
    with app.app_context():
        init_models()