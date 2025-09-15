from pydantic import BaseModel
from typing import Optional

class JobRequest(BaseModel):
    filename: str

class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    result_url: Optional[str] = None

class CertRequest(BaseModel):
    job_id: str
    user_id: str