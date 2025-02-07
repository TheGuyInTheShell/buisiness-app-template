from typing import List
from datetime import datetime
from pydantic import BaseModel



"""
    __tablename__ = 'orders'
 
    customer_id = Column(String, ForeignKey('customers.uid'))
    order_type = Column(Enum('delivery', 'pickup', 'dine_in', name='order_type'))
    order_date = Column(DateTime)
    total_amount = Column(String)
    status = Column(Enum('pending', 'in_progress', 'completed', 'cancelled', name='order_status'))
    payment_method = Column(Enum('cash', 'credit_card', 'debit_card', 'digital_wallet', name='payment_method'))
    table_id = Column(String, ForeignKey('tables.uid'))

"""

from core.schemas import Pagination



class RQOrders(BaseModel):
    customer_id: str
    order_type: str
    order_date: datetime
    total_amount: str
    status: str
    payment_method: str 


class RSOrders(RQOrders):
    uid: str

class RSOrdersList(Pagination):
    data: list[RSOrders] | List = []