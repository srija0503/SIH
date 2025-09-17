from pydantic import BaseModel

class History(BaseModel):
    job_id: str
    user_id: str
    status: str