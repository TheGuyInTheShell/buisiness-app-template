from sqlalchemy import (
    Date, ForeignKey, Column, Integer, String
)
from core.database.base import BaseAsync

class Revenue(BaseAsync):
    __tablename__ = 'revenue'
    order_id = Column(String, ForeignKey('orders.uid'))
    amount = Column(String)
    date = Column(Date)