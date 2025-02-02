from typing import Literal, Optional
from core.services.generic_controller import get_some

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db

from .models import Delivery
from .schemas import RQDelivery, RSDelivery, RSDeliveryList

# prefix /customers
router = APIRouter(tags = ['customers'])

@router.get("id/{id}", response_model=RSDelivery, status_code=200)
async def get_customer(id: str, db: AsyncSession = Depends(get_async_db)) -> RSDelivery:
    try:
        result = await Delivery.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSDeliveryList, status_code=200)
async def get_customers(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSDeliveryList:
    try:
        result = await get_some(
            db=db,
            Model=Delivery,
            Schema=RSDelivery,
            SchemaList=RSDeliveryList,
            query={
                "pag": pag,
                "order": ord,
                "status": status,
            })
        return result
    except Exception as e:
        print(e)
        raise e


@router.post("/", response_model=RSDelivery, status_code=201)
async def create_customer(
    delivery: RQDelivery, db: AsyncSession = Depends(get_async_db)
) -> RSDelivery:
    try:
        result = await Delivery(**delivery.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204)
async def delete_customer(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Delivery.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSDelivery, status_code=200)
async def update_customer(
    id: str, delivery: RQDelivery, db: AsyncSession = Depends(get_async_db)
) -> RSDelivery:
    try:
        result = await Delivery.update(db, id, delivery.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
