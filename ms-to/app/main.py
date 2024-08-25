from fastapi import FastAPI
from app.routers.endpoints import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="ms-to",
    summary="takes request",
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
