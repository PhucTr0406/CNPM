from sqlalchemy import Column, BIGINT, String, DateTime, ForeignKey, Integer, Numeric, Date
from .base_model import Base
import datetime

class SubscriptionModel(Base):
    __tablename__ = 'SUBSCRIPTION'
    subscription_id = Column(BIGINT, primary_key=True, autoincrement=True)
    account_id = Column(BIGINT, ForeignKey('ACCOUNT.account_id'))
    
    # Lưu ý: Nếu bạn chưa có bảng SERVICE_PACKAGE, hãy tạo Model cho nó 
    # hoặc tạm thời comment ForeignKey này lại để tránh lỗi khởi tạo.
    package_id = Column(Integer, ForeignKey('SERVICE_PACKAGE.package_id'))
    
    start_date = Column(Date, default=datetime.date.today)
    end_date = Column(Date)
    remaining_credits = Column(Integer)

class PaymentModel(Base):
    __tablename__ = 'PAYMENT'
    payment_id = Column(BIGINT, primary_key=True, autoincrement=True)
    subscription_id = Column(BIGINT, ForeignKey('SUBSCRIPTION.subscription_id'))
    
    # Sửa Decimal(12, 2) thành Numeric(12, 2)
    amount = Column(Numeric(12, 2)) 
    
    payment_time = Column(DateTime, default=datetime.datetime.utcnow)