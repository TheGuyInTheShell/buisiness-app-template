from typing import Literal, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_db
from core.services.generic_controller import get_some
from .models import Inventory
from .schemas import RQInventory, RSInventory, RSInventoryList

router = APIRouter(tags = ['inventory'])

@router.get("id/{id}", response_model=RQInventory)
async def get_inventory(id: str, db: AsyncSession = Depends(get_async_db)):
    try:
        return await Inventory.find_one(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=RSInventoryList)
async def get_paged_inventory(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
):
    try:
        result = await get_some(
            Inventory,
            RQInventory,
            RSInventoryList,
            db,
            query={
                "pag": pag,
                "ord": ord,
                "status": status,
            }
        )
        return result 
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=RSInventory, status_code=201)
async def create_inventory(
    inventory: RQInventory, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Inventory(**inventory.model_dump()).save(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("id/{id}", response_model=RSInventory)
async def update_inventory(
    id: str,
    inventory: RQInventory,
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Inventory.update(db, id, inventory.model_dump())
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("id/{id}", status_code=204)
async def delete_inventory(
    id: str, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        await Inventory.delete(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))