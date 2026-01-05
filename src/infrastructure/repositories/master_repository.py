from .base_repository import BaseRepository
from infrastructure.models.master_data_model import ServicePackageModel, AIModelVersionModel
from infrastructure.models.clinic_model import ClinicModel

class ServicePackageRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, ServicePackageModel)

class AIModelVersionRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, AIModelVersionModel)

    def get_latest_version(self):
        return self.session.query(AIModelVersionModel).order_by(AIModelVersionModel.ai_model_version_id.desc()).first()

class ClinicRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, ClinicModel)