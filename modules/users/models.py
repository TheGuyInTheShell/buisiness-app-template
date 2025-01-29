from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.base import BaseAsync
from modules.roles.models import Role


class User(BaseAsync):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    role_ref: Mapped[str] = mapped_column(String, ForeignKey('roles.uid'), nullable=False) 
    role: Mapped[Role] = relationship("Role")
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
