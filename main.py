from routers.user_services import router
from app import app

app.include_router(router.router, prefix="/users", tags=["Users"])