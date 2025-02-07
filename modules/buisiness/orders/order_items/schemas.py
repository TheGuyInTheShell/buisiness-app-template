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


class RQMenuItem(BaseModel):
    customer_id: str
    order_type: str
    order_date: datetime
    total_amount: str
    status: str
    payment_method: str 


class RSMenuItem(RQMenuItem):
    uid: str

class RSMenuItemList(BaseModel):
    data: list[RSMenuItem] | List = []
    total: int = 0
    page: int = 0
    page_size: int = 0
    total_pages: int = 0
    has_next: bool = False
    has_prev: bool = False
    next_page: int = 0
    prev_page: int = 0