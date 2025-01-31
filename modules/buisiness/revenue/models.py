from sqlalchemy import (
    Date, ForeignKey, Column, Integer, String
)
from core.database.base import BaseAsync

class Revenue(BaseAsync):
    __tablename__ = 'revenue'
    order_id = Column(Integer, ForeignKey('orders.id'))
    amount = Column(String)
    date = Column(Date)