from typing import List

from pydantic import BaseModel
from core.schemas import Pagination


"""class Delivery(BaseAsync):
    __tablename__ = 'deliveries'
    
    order_id = Column(Integer, ForeignKey('orders.uid'))
    delivery_person_id = Column(Integer, ForeignKey('employees.id'))
    address = Column(String)
    delivery_time = Column(DateTime)
    status = Column(String)"""

class RQCustomer(BaseModel):
    order_id: str
    phone: str
    email: str
    address: str

class RSCustomer(RQCustomer):
    uid: str

class RSCustomerList(Pagination):
    data: list[RSCustomer] | List = []