from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
import logging
import sys

from app.services.add import add

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler that writes to stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(stdout_handler)

# If you still want to keep file logging, you can add a file handler as well
file_handler = logging.FileHandler('/var/log/ms-from_router.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

router = APIRouter()

@router.post("/add_counter")
async def add_counter(counter: int, amount: int) -> int:
    confirmation = await add(counter, amount)
    if confirmation is None:
        logger.error(f"User not found for counter: {counter}")
        raise HTTPException(status_code=404, detail="usuario no encontrado")

    logger.info(f"Counter added successfully: counter={counter}, amount={amount}")
    return JSONResponse(content=confirmation)
