from typing import TYPE_CHECKING
from sqlalchemy import (
    Date, Column, String
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync

if TYPE_CHECKING:
    from modules.buisiness.delivery.models import Delivery

class Employee(BaseAsync):
    __tablename__ = 'employees'
    name = Column(String)
    role = Column(String)
    phone = Column(String)
    hire_date = Column(Date)