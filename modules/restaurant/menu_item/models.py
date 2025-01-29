from sqlalchemy.orm import Mapped, mapped_column
from core.database.base import BaseAsync
from sqlalchemy import Numeric, Text
from typing import Optional

class MenuItem(BaseAsync):
    __tablename__ = 'menu_items'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]]
    description: Mapped[Optional[Text]]
    price: Mapped[Optional[Numeric]]
    category: Mapped[Optional[str]]
    is_available: Mapped[Optional[bool]]

    order_items: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='menu_item')
