

"""
    __tablename__ = 'reservations'
    customer_id = Column(String, ForeignKey('customers.uid'))
    table_id = Column(String, ForeignKey('tables.uid'))
    reservation_time = Column(DateTime)
    party_size = Column(Integer)

"""

from typing import List
from datetime import datetime
from pydantic import BaseModel


from core.schemas import Pagination

class RQReservations(BaseModel):
    customer_id: str
    table_id = str
    reservation_time: datetime
    party_size: int

class RSReservations(RQReservations):
    uid: str

class RSReservationsList(Pagination):
    data: list[RSReservations] | List = []