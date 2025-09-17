# backend/engine/logger.py

import datetime

def log_event(message):
    """
    Log an event with a timestamp to stdout and 'engine.log'.
    """
    ts = datetime.datetime.now().isoformat()
    log_message = f"[{ts}] {message}"
    print(log_message)
    with open("engine.log", "a") as f:
        f.write(log_message + "\n")