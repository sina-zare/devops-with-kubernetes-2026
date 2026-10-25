
import os
import uvicorn
from fastapi import FastAPI

PORT = int(os.getenv("PORT", "8080"))

app = FastAPI()
    

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Todo App</title>
    </head>
    <body>
        <h1>Todo App</h1>
        <p>The application is running successfully.</p>
    </body>
    </html>
    """
    


print(f"Server started in port {PORT}", flush=True)
uvicorn.run(app, host="0.0.0.0", port=PORT)