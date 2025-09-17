from fastapi import APIRouter, UploadFile, File
from .models import JobStatusResponse
from .storage import save_job, get_job_status
from uuid import uuid4

router = APIRouter()

@router.post("/create", response_model=JobStatusResponse)
async def create_job(file: UploadFile = File(...)):
    job_id = str(uuid4())
    save_job({"job_id": job_id, "status": "pending", "filename": file.filename})
    # Would trigger worker/engine here
    return JobStatusResponse(job_id=job_id, status="pending")

@router.get("/{job_id}", response_model=JobStatusResponse)
def job_status(job_id: str):
    status = get_job_status(job_id)
    return JobStatusResponse(job_id=job_id, status=status)