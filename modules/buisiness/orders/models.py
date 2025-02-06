from sqlalchemy import Enum, ForeignKey, DateTime, Column, String 
from core.database.base import BaseAsync

class Order(BaseAsync):
    __tablename__ = 'orders'
 
    customer_id = Column(String, ForeignKey('customers.uid'))
    order_type = Column(Enum('delivery', 'pickup', 'dine_in', name='order_type'))
    order_date = Column(DateTime)
    total_amount = Column(String)
    status = Column(Enum('pending', 'in_progress', 'completed', 'cancelled', name='order_status'))
    payment_method = Column(Enum('cash', 'credit_card', 'debit_card', 'transference ', name='payment_method'))
    table_id = Column(String, ForeignKey('tables.uid'))
