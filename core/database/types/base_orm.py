from abc import ABC, abstractmethod
from typing import Any, List, Sequence, Set, Literal, Generic, TypeVar
from sqlalchemy import ColumnElement
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T', bound='AsyncRepository')

class AsyncRepository(ABC, Generic[T]):
    
    @abstractmethod
    async def save(self: T, db: AsyncSession) -> T:
        pass
    
    @abstractmethod
    @classmethod
    async def delete(cls, db: AsyncSession, id: int | str) -> T:
        pass
    
    @abstractmethod
    @classmethod
    async def update(cls, db: AsyncSession, id: int | str, data: dict) -> T:
        pass
    
    @abstractmethod
    @classmethod
    async def find_one(cls, db: AsyncSession, id: int | str) -> T:
        pass
    
    @abstractmethod
    @classmethod
    async def find_some(
        cls,
        db: AsyncSession,
        pag: int = 1,
        ord: str = 'asc',
        status: Literal["deleted", "exists", "all"] = 'all',
        filters: Set[ColumnElement] = None
    ) -> List[T]:
        pass
    
    @abstractmethod
    @classmethod
    async def find_by_column(cls, db: AsyncSession, column: str, value: Any) -> List[T]:
        pass
    
    @abstractmethod
    @classmethod
    async def find_by_specification(cls, db: AsyncSession, specification: dict) -> List[T]:
        pass
    
    @abstractmethod
    @classmethod
    def touple_to_dict(cls, arr: Sequence[T]) -> List[T]:
        pass
    
    @abstractmethod
    @classmethod
    def get_deleted(cls) -> Any:
        pass
    
    @abstractmethod
    @classmethod
    def get_exists(cls) -> Any:
        pass