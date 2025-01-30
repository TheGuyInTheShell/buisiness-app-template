from typing import Optional, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync

if TYPE_CHECKING:
    from modules.restaurant.orders.models import Order
    from modules.restaurant.tables.reservations.models import Reservation

class Table(BaseAsync):
    __tablename__ = 'tables'
    table_number: Mapped[Optional[int]]
    capacity: Mapped[Optional[int]]
    status: Mapped[Optional[str]]

    orders: Mapped[list['Order']] = relationship('Order', back_populates='table')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='table')
