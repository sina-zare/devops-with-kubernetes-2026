import os
import random
import string
import time
import threading
import uvicorn
from datetime import datetime, timezone
from fastapi import FastAPI

PORT = int(os.getenv("PORT", "8787"))
app = FastAPI()

section_one = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
section_two = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
section_three = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

random_string = f'{section_one}-{section_two}-{section_three}'

# Shared application status
status = {
    "timestamp": None,
    "random_string": random_string
}
status_lock = threading.Lock()


def log_output():
    while True:
        timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

        with status_lock:
            status["timestamp"] = timestamp

        print(f'{timestamp}: {random_string}')
        time.sleep(5)

@app.get("/")
def home():
    with status_lock:
        return status.copy()


# Run the logging loop in a background thread
logging_thread = threading.Thread(
    target=log_output,
    daemon=True
)
logging_thread.start()

print(f"Server started on port {PORT}", flush=True)

uvicorn.run(app, host="0.0.0.0", port=PORT)