from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from .models import JobRequest, JobStatusResponse, CertRequest
from .storage import save_job, get_job_status
from .worker_client import enqueue_job
from .cert_routes import router as cert_router
from .jobs_routes import router as jobs_router

app = FastAPI(title="DataNirvana API")

app.include_router(jobs_router, prefix="/jobs")
app.include_router(cert_router, prefix="/cert")

@app.get("/")
def root():
    return {"status": "API Running"}