from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import Order
from .schemas import RQOrders, RSOrders, RSOrdersList

# prefix /menu
router = APIRouter()
tag = 'menu'

@router.get("id/{id}", response_model=RSOrders, status_code=200, tags=[tag])
async def get_order(id: str, db: AsyncSession = Depends(get_async_db)) -> RSOrders:
    try:
        result = await Order.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSOrdersList, status_code=200, tags=[tag])
async def get_orders(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSOrdersList:
    try:
        result = await get_some(
            Order,
            RQOrders,
            RSOrdersList,
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


@router.post("/", response_model=RSOrders, status_code=201, tags=[tag])
async def create_order(
    menu: RQOrders, db: AsyncSession = Depends(get_async_db)
) -> RSOrders:
    try:
        result = await Order(**menu.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_order(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Order.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSOrders, status_code=200, tags=[tag])
async def update_order(
    id: str, menu: RQOrders, db: AsyncSession = Depends(get_async_db)
) -> RSOrders:
    try:
        result = await Order.update(db, id, menu.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
