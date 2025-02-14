from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import Table
from .schemas import RQTables, RSTables, RSTablesList

# prefix /table
router = APIRouter()
tag = 'table'

@router.get("id/{id}", response_model=RSTables, status_code=200, tags=[tag])
async def get_table(id: str, db: AsyncSession = Depends(get_async_db)) -> RSTables:
    try:
        result = await Table.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSTablesList, status_code=200, tags=[tag])
async def get_tables(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSTablesList:
    try:
        result = await get_some(
            Table,
            RQTables,
            RSTablesList,
            db,
            query={
                "pag": pag,
                "ord": ord,
                "status": status,
            }
        )
        return result 
    except Exception as e:
        print(e)
        raise e


@router.post("/", response_model=RSTables, status_code=201, tags=[tag])
async def create_table(
    data: RQTables, db: AsyncSession = Depends(get_async_db)
) -> RSTables:
    try:
        result = await Table(**data.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_table(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Table.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSTables, status_code=200, tags=[tag])
async def update_table(
    id: str, data: RQTables, db: AsyncSession = Depends(get_async_db)
) -> RSTables:
    try:
        result = await Table.update(db, id, data.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
