from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import OrderItem
from .schemas import RQOrderItem, RSOrderItem, RSOrderItemList

# prefix /order_item
router = APIRouter()
tag = 'order_item'

@router.get("id/{id}", response_model=RSOrderItem, status_code=200, tags=[tag])
async def get_order_item(id: str, db: AsyncSession = Depends(get_async_db)) -> RSOrderItem:
    try:
        result = await OrderItem.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSOrderItemList, status_code=200, tags=[tag])
async def get_order_items(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSOrderItemList:
    try:
        result = await get_some(
            OrderItem,
            RQOrderItem,
            RSOrderItemList,
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


@router.post("/", response_model=RSOrderItem, status_code=201, tags=[tag])
async def create_order_item(
    order_item: RQOrderItem, db: AsyncSession = Depends(get_async_db)
) -> RSOrderItem:
    try:
        result = await OrderItem(**order_item.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_order_item(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await OrderItem.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSOrderItem, status_code=200, tags=[tag])
async def update_order_item(
    id: str, order_item: RQOrderItem, db: AsyncSession = Depends(get_async_db)
) -> RSOrderItem:
    try:
        result = await OrderItem.update(db, id, order_item.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
