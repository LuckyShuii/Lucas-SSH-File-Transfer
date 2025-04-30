from fastapi import APIRouter

router = APIRouter(prefix="/api/tag",tags=["tag"],responses={404: {"description": "Not found"}})

@router.get("/all")
async def get_all_tags():
    return "response"