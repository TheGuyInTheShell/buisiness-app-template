from typing import Optional
from sqlalchemy.orm import Mapped
from core.database.base import BaseAsync


class Supplier(BaseAsync):
    __tablename__ = 'suppliers'
    name: Mapped[Optional[str]]
    contact: Mapped[Optional[str]]