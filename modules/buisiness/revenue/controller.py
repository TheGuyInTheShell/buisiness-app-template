from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import Revenue
from .schemas import RQRevenues, RSRevenues, RSRevenuesList

# prefix /revenue
router = APIRouter()
tag = 'revenue'

@router.get("id/{id}", response_model=RSRevenues, status_code=200, tags=[tag])
async def get_revenue(id: str, db: AsyncSession = Depends(get_async_db)) -> RSRevenues:
    try:
        result = await Revenue.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSRevenuesList, status_code=200, tags=[tag])
async def get_revenues(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSRevenuesList:
    try:
        result = await get_some(
            Revenue,
            RQRevenues,
            RSRevenuesList,
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


@router.post("/", response_model=RSRevenues, status_code=201, tags=[tag])
async def create_revenue(
    data: RQRevenues, db: AsyncSession = Depends(get_async_db)
) -> RSRevenues:
    try:
        result = await Revenue(**data.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_revenue(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Revenue.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSRevenues, status_code=200, tags=[tag])
async def update_revenue(
    id: str, data: RQRevenues, db: AsyncSession = Depends(get_async_db)
) -> RSRevenues:
    try:
        result = await Revenue.update(db, id, data.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
