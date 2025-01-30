from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, TYPE_CHECKING
from sqlalchemy import DateTime
from core.database.base import BaseAsync
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from modules.buisiness.orders.models import Order
    from modules.buisiness.tables.reservations.models import Reservation

class Customer(BaseAsync):
    __tablename__ = 'customers'
    name: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    address: Mapped[Optional[str]]

    orders: Mapped[list['Order']] = relationship('Order', back_populates='customer')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='customer')
