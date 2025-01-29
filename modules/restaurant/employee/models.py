from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    Date
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync

if TYPE_CHECKING:
    from modules.restaurant.delivery.models import Delivery

class Employee(BaseAsync):
    __tablename__ = 'employees'
    name: Mapped[Optional[str]]
    role: Mapped[Optional[str]]
    phone: Mapped[Optional[str]]
    hire_date: Mapped[Optional[Date]]

    deliveries: Mapped[list['Delivery']] = relationship('Delivery', back_populates='delivery_person')