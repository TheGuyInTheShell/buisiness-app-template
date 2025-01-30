from typing import Optional
from sqlalchemy import (
    Numeric, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.restaurant.orders.models import Order
    from modules.restaurant.menu_item.models import MenuItem


class OrderItem(BaseAsync):
    __tablename__ = 'order_items'
    order_id: Mapped[Optional[int]] = mapped_column(ForeignKey('orders.id'))
    menu_item_id: Mapped[Optional[int]] = mapped_column(ForeignKey('menu_items.id'))
    quantity: Mapped[Optional[int]]
    subtotal: Mapped[Optional[Numeric]]

    order: Mapped['Order'] = relationship('Order', back_populates='order_items')
    menu_item: Mapped['MenuItem'] = relationship('MenuItem', back_populates='order_items')
