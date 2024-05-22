from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def hello_api():
  return {"msg": "pong"}
