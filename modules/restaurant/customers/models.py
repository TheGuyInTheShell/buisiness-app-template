from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from sqlalchemy import DateTime
from core.database.base import BaseAsync
from sqlalchemy.orm import relationship
from modules.restaurant.orders.models import Order

class Customer(BaseAsync):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    address: Mapped[Optional[str]]
    created_at: Mapped[Optional[DateTime]]

    orders: Mapped[list['Order']] = relationship('Order', back_populates='customer')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='customer')
