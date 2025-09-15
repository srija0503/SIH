import json
JOB_STORE = "jobs.json"

def save_job(job):
    with open(JOB_STORE, "a") as f:
        f.write(json.dumps(job) + "\n")

def get_job_status(job_id):
    with open(JOB_STORE) as f:
        for line in f:
            job = json.loads(line)
            if job['job_id'] == job_id:
                return job['status']
    return "not found"