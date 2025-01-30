from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    Date, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync

if TYPE_CHECKING:
    from modules.buisiness.customers.models import Customer

class Revenue(BaseAsync):
    __tablename__ = 'revenue'
    order_id: Mapped[Optional[int]] = mapped_column(ForeignKey('orders.id'), nullable=True)
    amount: Mapped[int]
    order: Mapped['Customer'] = relationship('Order', back_populates='revenue')