from typing import Literal, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_db
from core.services.generic_controller import get_some
from .models import Expense
from .schemas import RQExpense, RQExpense, RSExpenseList

router = APIRouter(tags = ['expenses'])

@router.get("id/{id}", response_model=RQExpense)
async def get_expense(id: str, db: AsyncSession = Depends(get_async_db)):
    try:
        return await Expense.find_one(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=RSExpenseList)
async def get_expenses(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
):
    try:
        result = await get_some(
            Expense,
            RQExpense,
            RSExpenseList,
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

@router.post("/", response_model=RQExpense, status_code=201)
async def create_expense(
    expense: RQExpense, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Expense(**expense.model_dump()).save(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("id/{id}", response_model=RQExpense)
async def update_expense(
    id: str,
    expense: RQExpense,
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Expense.update(db, id, expense.model_dump())
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("id/{id}", status_code=204)
async def delete_expense(
    id: str, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        await Expense.delete(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))