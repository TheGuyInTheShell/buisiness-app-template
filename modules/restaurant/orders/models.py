from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
import enum
from sqlalchemy import Enum, Numeric, ForeignKey, DateTime
from core.database.base import BaseAsync
from sqlalchemy.orm import relationship


# Enumerations
class OrderStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class OrderType(enum.Enum):
    delivery = "delivery"
    pickup = "pickup"
    dine_in = "dine_in"


class Order(BaseAsync):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[Optional[int]] = mapped_column(ForeignKey('customers.id'))
    order_type: Mapped[Optional[OrderType]] = mapped_column(Enum(OrderType))
    order_date: Mapped[Optional[DateTime]]
    total_amount: Mapped[Optional[Numeric]]
    status: Mapped[Optional[OrderStatus]] = mapped_column(Enum(OrderStatus))
    payment_method: Mapped[Optional[PaymentMethod]] = mapped_column(Enum(PaymentMethod))
    table_id: Mapped[Optional[int]] = mapped_column(ForeignKey('tables.id'), nullable=True)

    customer: Mapped['Customer'] = relationship('Customer', back_populates='orders')
    table: Mapped[Optional['Table']] = relationship('Table', back_populates='orders')
    order_items: Mapped[list['OrderItem']] = relationship('OrderItem', back_populates='order')
    delivery: Mapped[Optional['Delivery']] = relationship('Delivery', back_populates='order', uselist=False)
    revenue: Mapped[Optional['Revenue']] = relationship('Revenue', back_populates='order', uselist=False)
