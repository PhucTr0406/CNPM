from .base_repository import BaseRepository
from infrastructure.models.account_model import AccountModel
from infrastructure.models.master_data_model import RoleModel, DoctorProfileModel

class AccountRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, AccountModel)

    def find_by_email(self, email):
        return self.session.query(AccountModel).filter(AccountModel.email == email).first()

    def find_by_username(self, username):
        return self.session.query(AccountModel).filter(AccountModel.username == username).first()

class RoleRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, RoleModel)

class DoctorProfileRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, DoctorProfileModel)

    def get_by_account_id(self, account_id):
        return self.session.query(DoctorProfileModel).filter(DoctorProfileModel.account_id == account_id).first()