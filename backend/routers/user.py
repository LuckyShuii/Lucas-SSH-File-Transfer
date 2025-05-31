from fastapi import APIRouter, Depends
from managers.user_manager import UserManager
from db.schemas.user_schema import UserCreate

router = APIRouter(prefix="/api/user",tags=["user"],responses={404: {"description": "Not found"}})

@router.post("/signup")
async def signup(payload: UserCreate, manager = Depends(UserManager())):
    return await manager.signup_user(payload)

@router.post("/activate_account/{token}")
async def activate_account(token: str, manager = Depends(UserManager())):
    return await manager.activate_account(token)