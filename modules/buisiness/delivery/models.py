from sqlalchemy import String, DateTime, ForeignKey, Column, Integer
from core.database.base import BaseAsync
from sqlalchemy.orm import relationship


def get_order_model():
    from modules.buisiness.orders.models import Order
    return Order

class Delivery(BaseAsync):
    __tablename__ = 'deliveries'
    
    order_id = Column(String, ForeignKey('orders.uid'))
    delivery_person_id = Column(String, ForeignKey('employees.uid'))
    address = Column(String)
    delivery_time = Column(DateTime)
    status = Column(String)

    order = relationship(get_order_model(), back_populates='delivery')

    def __init__(self, **kw):

        super().__init__(**kw)
        