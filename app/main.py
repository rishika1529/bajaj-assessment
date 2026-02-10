from fastapi import FastAPI
from routers.bhfl import router

app = FastAPI(
    title="BFHL API",
    version="1.2.1"
)

app.include_router(router)
