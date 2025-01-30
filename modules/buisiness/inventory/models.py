from typing import Optional
from sqlalchemy import (
    Numeric, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database.base import BaseAsync
from modules.buisiness.inventory.supliers.models import Supplier

class Inventory(BaseAsync):
    __tablename__ = 'inventory'
    item_name: Mapped[Optional[str]]
    quantity: Mapped[Optional[Numeric]]
    unit: Mapped[Optional[str]]
    reorder_level: Mapped[Optional[Numeric]]
    supplier_id: Mapped[Optional[int]] = mapped_column(ForeignKey('suppliers.id'))

    supplier: Mapped['Supplier'] = relationship('Supplier', back_populates='inventory_items')
