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

        return {
            "logs": lines
        }

    except FileNotFoundError:
        return {"logs": []}
    
uvicorn.run(app, host="0.0.0.0", port=PORT)