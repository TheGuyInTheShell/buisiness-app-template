from sqlalchemy import (
     DateTime, ForeignKey, Column, String, Integer
     )
from core.database.base import BaseAsync

class Reservation(BaseAsync):
    __tablename__ = 'reservations'
    customer_id = Column(String, ForeignKey('customers.uid'))
    table_id = Column(String, ForeignKey('tables.uid'))
    reservation_time = Column(DateTime)
    party_size = Column(Integer)

    
