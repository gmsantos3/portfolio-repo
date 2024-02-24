from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
import subprocess

app = FastAPI()

command = "/bin/echo 'hello, you have reached: ' && hostname -f"

result = subprocess.run(command, capture_output=True, text=True, shell=True)

@app.get("/")
def get_data():
    return PlainTextResponse(result.stdout)

uvicorn.run(app, host="0.0.0.0", port=8000)