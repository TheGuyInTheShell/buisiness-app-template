from sqlalchemy.orm import Mapped, relationship
from core.database.base import BaseAsync
from sqlalchemy import Numeric, Text
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.buisiness.orders.order_items.models import OrderItem

class MenuItem(BaseAsync):
    __tablename__ = 'menu_items'
    name: Mapped[Optional[str]]
    description: Mapped[Optional[Text]]
    price: Mapped[Optional[Numeric]]
    category: Mapped[Optional[str]]
    is_available: Mapped[Optional[bool]]

    order_items: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='menu_item')
