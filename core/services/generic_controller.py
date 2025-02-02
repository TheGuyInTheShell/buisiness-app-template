from core.database.base import BaseAsync
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import TypeVar, Union, Dict


T = TypeVar('T')
U = TypeVar('U')

class QueryType(Dict):
    pag: int
    ord: str
    status: str


async def get_some(
    Model: BaseAsync,
    Schema: Union[T, BaseModel],
    SchemaList: Union[U, BaseModel],
    db: AsyncSession,
    **query: QueryType
) ->  U: 
        """
        Fetches a paginated list of records from the database based on the provided filters.
        Args:
            Model (BaseAsync): The SQLAlchemy model class representing the database table.
            Schema (BaseModel): The Pydantic schema for validating and serializing individual records.
            SchemaList (BaseModel): The Pydantic schema for returning a paginated list of records.
            **kwargs: Additional keyword arguments for filtering and pagination:
                - pag (int, optional): The page number to fetch. Defaults to 1.
                - ord (str, optional): The order of results, either "asc" or "desc". Defaults to "asc".
                - status (str, optional): The status filter for records. Defaults to "exists".
                - db (Session, optional): The database session. Defaults to None.

        Returns:
            SchemaList: A paginated list of records wrapped in the provided SchemaList schema.
        """
        pag = query.get("pag", 1)
        ord = query.get("ord", "asc")
        status = query.get("status", "exists")
        result = await Model.find_some(db, pag, ord, status)
        keys = Schema.model_fields.keys()
        result = map(
            lambda x: Schema(
                **{key: getattr(x, key) for key in keys}
            ),
            result,
        )
        return SchemaList(
            data=list(result),
            total=0,
            page=0,
            page_size=0,
            total_pages=0,
            has_next=False,
            has_prev=False,
            next_page=0,
            prev_page=0,
        )