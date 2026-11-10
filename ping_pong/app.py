import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


PORT = int(os.getenv("PORT", "8181"))
app = FastAPI()
counter = 0

@app.get("/pingpong")
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1

    return response

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Ping pong</title>
    </head>
    <body>
        <h1>Oops!</h1>
        <p>Nothing here. Check /pingpong</p>
    </body>
    </html>
    """

uvicorn.run(app, host="0.0.0.0", port=PORT)