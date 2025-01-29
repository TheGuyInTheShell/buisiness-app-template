from datetime import datetime
from typing import Any, List, Self, Sequence, Literal
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
import uuid
import asyncio
from core.database.turso.async_connection import engine
from sqlalchemy import (
    TIMESTAMP,
    UUID,
    Boolean,
    Column,
    Integer,
    String,
    func,
    select,
    text,
    update,
)

def generate_uuid():
    return str(uuid.uuid4())

class BaseAsync(DeclarativeBase):
    
    uid: Mapped[str] = mapped_column(
        String,
        unique=True, 
        nullable=False, 
        index=True,  
        primary_key=True, 
        default=generate_uuid
    )
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.current_timestamp()
    )
    deleted_at: Mapped[datetime] = mapped_column(nullable=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def get_deleted(cls):
        return cls.deleted
    
    @classmethod
    def get_exists(cls):
        return cls.exists
    
    @classmethod
    async def touple_to_dict(cls, arr: Sequence[Self]) -> List[Self]:
        return [cls(**dict(row._mapping)) for row in arr]

    async def save(self, db: AsyncSession):
        db.add(self)
        await db.commit()
        await db.refresh(self)
        return self
    
    @classmethod
    async def create_global_views(cls):
        async with engine.begin() as conn:
            await conn.execute(text(
                f"CREATE VIEW IF NOT EXISTS {cls.__tablename__}_deleted AS "
                f"SELECT * FROM {cls.__tablename__} WHERE is_deleted = true"
            ))
            await conn.execute(text(
                f"CREATE VIEW IF NOT EXISTS {cls.__tablename__}_exists AS "
                f"SELECT * FROM {cls.__tablename__} WHERE is_deleted = false"
            ))
            await conn.commit()

    def __init_subclass__(cls) -> None:
        asyncio.run(cls.create_global_views())
        super().__init_subclass__()

    @classmethod
    async def delete(cls, db: AsyncSession, id: str):
        reg = await cls.find_one(db, id)
        await db.execute(
            update(cls)
            .where(cls.uid == id)
            .values(is_deleted=True, deleted_at=func.now())
        )
        await db.commit()
        return reg
    
    @classmethod
    async def update(cls, db: AsyncSession, id: str, data: dict):
        data["updated_at"] = func.now()
        await db.execute(
            update(cls)
            .where(cls.uid == id)
            .values(**data)
        )
        await db.commit()
        return await cls.find_one(db, id)
    
    @classmethod
    async def find_one(cls, db: AsyncSession, id: str) -> Self:
        result = await db.execute(
            select(cls)
            .where(cls.uid == id)
            .limit(1)
        )
        return result.scalars().first()
    
    @classmethod
    async def find_some(
        cls,
        db: AsyncSession,
        page: int = 1,
        per_page: int = 10,
        status: Literal["deleted", "exists", "all"] = "all"
    ) -> List[Self]:
        query = select(cls)
        
        if status == "deleted":
            query = query.where(cls.is_deleted == True)
        elif status == "exists":
            query = query.where(cls.is_deleted == False)
            
        result = await db.execute(
            query.order_by(cls.created_at.desc())
            .offset((page - 1) * per_page)
            .limit(per_page)
        )
        return result.scalars().all()
    
    @classmethod
    async def find_by_column(cls, db: AsyncSession, column: str, value: Any):
        result = await db.execute(
            select(cls).where(getattr(cls, column) == value)
        )
        return result.scalars().all()
    
class BaseSync(DeclarativeBase):
    uid: Mapped[str] = Column(String, unique=True, nullable=False, index=True,  primary_key=True, default=UUID())
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = Column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    is_deleted: Mapped[bool] = Column(Boolean, default=False)
    deleted_at: Mapped[datetime] = Column(TIMESTAMP, nullable=True)