from fastapi import APIRouter

router = APIRouter(prefix="/api",tags=["api"],responses={404: {"description": "Not found"}})

@router.get("/")
async def api():
    return {"status": "ok"}