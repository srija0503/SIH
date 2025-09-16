# backend/engine/core_wipe.py

import time
from .logger import log_event
from .persistence import save_job_result

def run_job(job_id, filename):
    """
    Simulate running a job on a file (e.g., wipe, detection).
    """
    log_event(f"Job {job_id}: Started processing {filename}")
    # Simulate processing time
    time.sleep(2)
    result = {
        "job_id": job_id,
        "filename": filename,
        "status": "completed",
        "output": f"Results for {filename} (simulated)"
    }
    save_job_result(result)
    log_event(f"Job {job_id}: Completed")
    return result

def queue_consumer(jobs_queue):
    """
    Continuously process jobs from the given jobs_queue list.
    jobs_queue is a list of dicts with 'job_id' and 'filename'.
    """
    log_event("Queue consumer started.")
    while True:
        if not jobs_queue:
            time.sleep(1)
            continue
        job = jobs_queue.pop(0)
        run_job(job['job_id'], job['filename'])