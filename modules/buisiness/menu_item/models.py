from sqlalchemy.orm import Mapped, relationship, mapped_column
from core.database.base import BaseAsync
from sqlalchemy import Text, Column, String, Boolean

class MenuItems(BaseAsync):
    __tablename__ = 'menu_items'
    name = Column(String)
    description = Column(Text)
    price = Column(String)
    category = Column(String)
    is_available = Column(Boolean)
