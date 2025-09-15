def enqueue_job(job_data):
    # Simulate job queueing, in real use would use Redis/RQ/Celery etc.
    print(f"Job enqueued: {job_data}")
    return True