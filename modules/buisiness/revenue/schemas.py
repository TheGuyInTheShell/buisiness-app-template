from typing import List
from datetime import datetime
from pydantic import BaseModel



"""
    __tablename__ = 'revenue'
    order_id = Column(String, ForeignKey('orders.uid'))
    amount = Column(String)
    date = Column(Date)

"""

from core.schemas import Pagination



class RQRevenues(BaseModel):
    order_id: str
    amount: int
    date: datetime

class RSRevenues(RQRevenues):
    uid: str

class RSRevenuesList(Pagination):
    data: list[RSRevenues] | List = []