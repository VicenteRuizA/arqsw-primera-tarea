from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse

from app.services.add import add


router = APIRouter()


@router.post("/add_counter")
async def add_counter(counter: int, amount: int) -> int:
    confirmation = await add(counter, amount)
    if confirmation is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")

    return JSONResponse(content=confirmation)

