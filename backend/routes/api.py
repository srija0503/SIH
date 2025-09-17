from fastapi import APIRouter
from ..controllers.uploadController import router as upload_router

router = APIRouter()
router.include_router(upload_router, prefix="/upload")