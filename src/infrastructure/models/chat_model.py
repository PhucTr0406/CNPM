from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Text
from .base_model import Base
import datetime

class ConversationModel(Base):
    __tablename__ = 'CONVERSATION'
    conversation_id = Column(BIGINT, primary_key=True, autoincrement=True)
    patient_id = Column(BIGINT, ForeignKey('PATIENT_PROFILE.patient_id'))
    doctor_id = Column(BIGINT, ForeignKey('DOCTOR_PROFILE.doctor_id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class MessageModel(Base):
    __tablename__ = 'MESSAGE'
    message_id = Column(BIGINT, primary_key=True, autoincrement=True)
    conversation_id = Column(BIGINT, ForeignKey('CONVERSATION.conversation_id'))
    sender_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    message_text = Column(Text)
    sent_at = Column(DateTime, default=datetime.datetime.utcnow)