from fastapi import APIRouter, HTTPException
from .models import CertRequest

router = APIRouter()

@router.post("/generate")
def generate_cert(req: CertRequest):
    # Call cert_generator from security/
    # Here, just simulate success
    return {"msg": "Certificate generated", "job_id": req.job_id}