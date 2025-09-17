from fastapi import APIRouter
from ..controllers.historyController import router as history_router

router = APIRouter()
router.include_router(history_router)