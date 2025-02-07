from sqlalchemy import (
    Column, ForeignKey, String, 
)
from sqlalchemy.dialects.mysql import INTEGER
from core.database.base import BaseAsync

class OrderItem(BaseAsync):
    __tablename__ = 'order_items'

    order_id = Column(String, ForeignKey('orders.uid'))
    menu_item_id = Column(String, ForeignKey('menu_items.uid'))
    quantity = Column(INTEGER(unsigned=True), default=1, nullable=False, )
    subtotal = Column(String)

