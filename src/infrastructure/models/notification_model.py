from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Boolean
from .base_model import Base
import datetime

class NotificationModel(Base):
    __tablename__ = 'NOTIFICATION'
    notification_id = Column(BIGINT, primary_key=True, autoincrement=True)
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    title = Column(String(255))
    content = Column(String(1000))
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)