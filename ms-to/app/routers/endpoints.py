from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.services.add import add_counter

router = APIRouter()

class AddRequest(BaseModel):
    counter: int
    amount: int

@router.post("/add")
async def add(request: AddRequest) -> int:
    addition = await add_counter(request.counter, request.amount)
    if addition is None:
        raise HTTPException(status_code=404, detail="Fallo al intentar sumar al contador")

    return JSONResponse(content=addition)

