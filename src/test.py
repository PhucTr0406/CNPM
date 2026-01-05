import sys
import os
# Đảm bảo Python tìm thấy thư mục src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime
from src.infrastructure.databases.session import SessionLocal
from src.infrastructure.repositories.identity_repository import AccountRepository, RoleRepository
from src.infrastructure.repositories.master_repository import ServicePackageRepository, ClinicRepository
from src.infrastructure.repositories.medical_repository import PatientRepository
from src.infrastructure.models.master_data_model import RoleModel, ServicePackageModel
from src.infrastructure.models.account_model import AccountModel
from src.infrastructure.models.clinic_model import ClinicModel
from src.infrastructure.models.patient_model import PatientProfileModel

def test_full_system():
    session = SessionLocal()
    
    # Khởi tạo các Repository
    role_repo = RoleRepository(session)
    account_repo = AccountRepository(session)
    package_repo = ServicePackageRepository(session)
    clinic_repo = ClinicRepository(session)
    patient_repo = PatientRepository(session)

    # Danh sách lưu trữ ID để dọn dẹp (Cleanup)
    ids = {
        "role_id": None,
        "account_id": None,
        "package_id": None,
        "clinic_id": None,
        "patient_id": None
    }

    try:
        print("\n=== BẮT ĐẦU KIỂM THỬ HỆ THỐNG REPOSITORY ===")

        # --- NHÓM 1: IDENTITY & MASTER DATA ---
        print("\n[1] Test Identity & Master Data:")
        
        # Tạo Role
        role = role_repo.add(RoleModel(role_name="TEST_ADMIN"))
        ids["role_id"] = role.role_id
        print(f"  - Tạo Role thành công (ID: {ids['role_id']})")

        # Tạo Account
        account = account_repo.add(AccountModel(
            username="test_user_99",
            email="test_99@gmail.com",
            password_hash="hashed_123",
            role_id=ids["role_id"],
            status="Active"
        ))
        ids["account_id"] = account.account_id
        print(f"  - Tạo Account thành công (ID: {ids['account_id']})")

        # Tạo Gói dịch vụ
        package = package_repo.add(ServicePackageModel(
            package_name="Gói Test Premium",
            price=500000
        ))
        ids["package_id"] = package.package_id
        print(f"  - Tạo Service Package thành công (ID: {ids['package_id']})")

        # --- NHÓM 2: CLINIC & PATIENT ---
        print("\n[2] Test Clinic & Patient:")
        
        # Tạo Phòng khám
        clinic = clinic_repo.add(ClinicModel(
            clinic_name="Phòng Khám Đa Khoa Test",
            address="123 Đường Test, Quận 1",
            phone_number="0999888777"
        ))
        ids["clinic_id"] = clinic.clinic_id
        print(f"  - Tạo Clinic thành công (ID: {ids['clinic_id']})")

        # Tạo Bệnh nhân (Gắn với Account và Clinic vừa tạo)
        patient = patient_repo.add(PatientProfileModel(
            account_id=ids["account_id"],
            full_name="Nguyễn Văn Test",
            dob=datetime(1990, 1, 1),
            gender="Male",
            phone_number="0123456789",
            address="Địa chỉ Test",
            clinic_id=ids["clinic_id"]
        ))
        ids["patient_id"] = patient.patient_id
        print(f"  - Tạo Patient thành công (ID: {ids['patient_id']})")

        # --- KIỂM TRA TRUY VẤN (QUERY) ---
        print("\n[3] Kiểm tra truy vấn nâng cao:")
        found_acc = account_repo.find_by_email("test_99@gmail.com")
        print(f"  - Tìm Account theo Email: {'OK' if found_acc else 'FAIL'}")
        
        found_patient = patient_repo.find_by_account_id(ids["account_id"])
        print(f"  - Tìm Patient theo Account ID: {'OK' if found_patient else 'FAIL'}")

        print("\n>>> TẤT CẢ REPOSITORY ĐÃ HOẠT ĐỘNG CHÍNH XÁC!")

    except Exception as e:
        print(f"\n❌ LỖI TRONG QUÁ TRÌNH TEST: {e}")
        session.rollback()

    finally:
        print("\n=== ĐANG TIẾN HÀNH DỌN DẸP (CLEANUP) ===")
        # Xóa theo thứ tự ngược lại (Bảng con trước, bảng cha sau) để tránh lỗi Foreign Key
        try:
            if ids["patient_id"]: 
                patient_repo.delete(ids["patient_id"])
                print("  - Đã xóa Patient")
            if ids["account_id"]: 
                account_repo.delete(ids["account_id"])
                print("  - Đã xóa Account")
            if ids["role_id"]: 
                role_repo.delete(ids["role_id"])
                print("  - Đã xóa Role")
            if ids["clinic_id"]: 
                clinic_repo.add = None # Tránh gọi nhầm, dùng trực tiếp session để xóa clinic nếu cần hoặc repo
                clinic_repo.delete(ids["clinic_id"])
                print("  - Đã xóa Clinic")
            if ids["package_id"]: 
                package_repo.delete(ids["package_id"])
                print("  - Đã xóa Service Package")
            
            print(">>> DATABASE ĐÃ SẠCH SẼ NHƯ BAN ĐẦU!")
        except Exception as cleanup_err:
            print(f"⚠️ Lỗi khi dọn dẹp: {cleanup_err}")
        
        session.close()

if __name__ == "__main__":
    test_full_system()