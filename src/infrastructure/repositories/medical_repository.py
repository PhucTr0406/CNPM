from .base_repository import BaseRepository
from infrastructure.models.patient_model import PatientProfileModel
from infrastructure.models.image_model import RetinalImageModel
from infrastructure.models.ai_model import AIAnalysisModel, AIResultModel, AIAnnotationModel

class PatientRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, PatientProfileModel)

    def find_by_account_id(self, account_id):
        return self.session.query(PatientProfileModel).filter(PatientProfileModel.account_id == account_id).first()

class ImageRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, RetinalImageModel)

class AIRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, AIAnalysisModel)

    def get_results_by_analysis(self, analysis_id):
        return self.session.query(AIResultModel).filter(AIResultModel.analysis_id == analysis_id).all()

    def get_annotations_by_analysis(self, analysis_id):
        return self.session.query(AIAnnotationModel).filter(AIAnnotationModel.analysis_id == analysis_id).all()