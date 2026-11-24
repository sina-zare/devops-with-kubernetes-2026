from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()
PORT = int(os.getenv("PORT", "8787"))

@app.get("/")
def home():
    try:
        with open("/shared/log.txt", "r") as file:
            lines = file.readlines()
        with open("/data/pingpong.txt", "r") as counter_file:
            counter = counter_file.read().strip()
            
        return {
            "logs": lines,
            "counter": f"Ping / Pongs: {counter}"
        }

    except FileNotFoundError:
        return {"logs": [], "counter": "Ping / Pongs: 0"}
    
uvicorn.run(app, host="0.0.0.0", port=PORT)