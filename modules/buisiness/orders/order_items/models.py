from sqlalchemy import (
    Column, ForeignKey, Integer, String
)
from core.database.base import BaseAsync

class OrderItems(BaseAsync):
    __tablename__ = 'order_items'

    order_id = Column(String, ForeignKey('orders.uid'))
    menu_item_id = Column(String, ForeignKey('menu_items.uid'))
    quantity = Column(Integer)
    subtotal = Column(String)

