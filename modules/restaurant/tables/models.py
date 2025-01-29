from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync
from modules.restaurant.orders.models import Order
from modules.restaurant.tables.reservations.models import Reservation

class Table(BaseAsync):
    __tablename__ = 'tables'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    table_number: Mapped[Optional[int]]
    capacity: Mapped[Optional[int]]
    status: Mapped[Optional[str]]

    orders: Mapped[list['Order']] = relationship('Order', back_populates='table')
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='table')
