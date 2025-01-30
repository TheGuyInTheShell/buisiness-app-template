from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.buisiness.orders.models import Order
    from modules.buisiness.employee.models import Employee

class Delivery(BaseAsync):
    __tablename__ = 'deliveries'

    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    delivery_person_id: Mapped[int] = mapped_column(ForeignKey('employees.id'))
    address: Mapped[str] = mapped_column(String)
    delivery_time: Mapped[DateTime] = mapped_column()
    status: Mapped[str] = mapped_column(String)

    order: Mapped['Order'] = relationship('Order', back_populates='delivery')
    delivery_person: Mapped['Employee'] = relationship('Employee', back_populates='deliveries')