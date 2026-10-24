
import os
import uvicorn
from fastapi import FastAPI

PORT = int(os.environ.get("PORT", "8080"))

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Todo app is running!"}


print(f"Server started in port {PORT}", flush=True)
uvicorn.run(app, host="0.0.0.0", port=PORT)