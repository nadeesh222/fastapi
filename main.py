from pathlib import Path
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routes import router
from app.database import Base,engine

app = FastAPI()

app.include_router(router)

@app.get("/hello")
def hello():
    return {"messege":"Hello World"}



@app.get("/wellcome")
def welcome():
    return {"messege":"Hi KKK"}

BASE_DIR = Path(__file__).resolve().parent
Base.metadata.create_all(bind=engine)

@app.get("/", include_in_schema=False)
def show_frontend():
    return FileResponse(BASE_DIR / "index.html")



if __name__== "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)