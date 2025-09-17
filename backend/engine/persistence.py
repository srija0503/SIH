# backend/engine/persistence.py

import json
import os

RESULTS_FILE = "job_results.json"

def save_job_result(result):
    """
    Save a job result to a JSON file (append to list).
    """
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "w") as f:
            json.dump([], f)
    # Read, append, and write back
    with open(RESULTS_FILE, "r+") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
        data.append(result)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def get_job_results():
    """
    Read all job results from the JSON file.
    """
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []