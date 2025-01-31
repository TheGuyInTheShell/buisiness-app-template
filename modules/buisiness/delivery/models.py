from sqlalchemy import String, DateTime, ForeignKey, Column, Integer
from core.database.base import BaseAsync


class Delivery(BaseAsync):
    __tablename__ = 'deliveries'
    
    order_id = Column(Integer, ForeignKey('orders.id'))
    delivery_person_id = Column(Integer, ForeignKey('employees.id'))
    address = Column(String)
    delivery_time = Column(DateTime)
    status = Column(String)