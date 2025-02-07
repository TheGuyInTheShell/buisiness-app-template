from typing import List
from datetime import datetime
from pydantic import BaseModel



"""
class OrderItems(BaseAsync):
    __tablename__ = 'order_items'

    order_id = Column(String, ForeignKey('orders.uid'))
    menu_item_id = Column(String, ForeignKey('menu_items.uid'))
    quantity = Column(Integer)
    subtotal = Column(String)

"""
from core.schemas import Pagination


class RQOrderItem(BaseModel):
    order_id: str
    menu_item_id: str
    quantity: int
    subtotal: str


class RSOrderItem(RQOrderItem):
    uid: str

class RSOrderItemList(Pagination):
    data: list[RSOrderItem] | List = []