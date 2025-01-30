from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
     DateTime, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync

if TYPE_CHECKING:
    from modules.restaurant.customers.models import Customer
    from modules.restaurant.tables.models import Table

class Reservation(BaseAsync):
    __tablename__ = 'reservations'
    customer_id: Mapped[Optional[int]] = mapped_column(ForeignKey('customers.id'))
    table_id: Mapped[Optional[int]] = mapped_column(ForeignKey('tables.id'))
    reservation_time: Mapped[Optional[DateTime]]
    party_size: Mapped[Optional[int]]

    customer: Mapped['Customer'] = relationship('Customer', back_populates='reservations')
    table: Mapped['Table'] = relationship('Table', back_populates='reservations')
