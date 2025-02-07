from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import Order
from .schemas import RQMenuItem, RSMenuItem, RSMenuItemList

# prefix /menu
router = APIRouter()
tag = 'menu'

@router.get("/id/{id}", response_model=RSMenuItem, status_code=200, tags=[tag])
async def get_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> RSMenuItem:
    try:
        result = await Order.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSMenuItemList, status_code=200, tags=[tag])
async def get_Permissions(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSMenuItemList:
    try:
        result = await get_some(
            Order,
            RQMenuItem,
            RSMenuItemList,
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


@router.post("/", response_model=RSMenuItem, status_code=201, tags=[tag])
async def create_Permission(
    menu: RQMenuItem, db: AsyncSession = Depends(get_async_db)
) -> RSMenuItem:
    try:
        result = await Order(**menu.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("/id/{id}", status_code=204, tags=[tag])
async def delete_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Order.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("/id/{id}", response_model=RSMenuItem, status_code=200, tags=[tag])
async def update_Permission(
    id: str, menu: RQMenuItem, db: AsyncSession = Depends(get_async_db)
) -> RSMenuItem:
    try:
        result = await Order.update(db, id, menu.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
