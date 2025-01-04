from fastapi import FastAPI
from routers.user_router import router as user_router
from config.database import engine, Base

app = FastAPI()

app.include_router(user_router, prefix="/api", tags=["Users"])

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "API is running!"}