from sqlalchemy import (
    Column, ForeignKey, Integer, String
)
from core.database.base import BaseAsync

class OrderItems(BaseAsync):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.uid'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.uid'))
    quantity = Column(Integer)
    subtotal = Column(String)

