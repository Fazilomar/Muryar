from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content=open("simulator.html").read())


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)
