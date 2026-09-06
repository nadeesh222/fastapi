from pathlib import Path
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return {"messege":"Hello World"}



@app.get("/wellcome")
def welcome():
    return {"messege":"Hi KKK"}

if __name__== "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)