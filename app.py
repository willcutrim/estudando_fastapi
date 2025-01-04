from fastapi import FastAPI
from models.user_models import Base
from config.database import engine

app = FastAPI()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    import uvicorn
    uvicorn.run(app, host=8000)