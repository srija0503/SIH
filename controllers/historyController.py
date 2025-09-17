from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_history():
    # Simulate user/job history
    return [{"job_id": "123", "status": "done"}]