from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
items = ["Apple","Orange","Banana" ]
#Run Command: uvicorn main:app --host 0.0.0.0 --por-reload 
#uvicorn main:app --reload
# http://localhost:8000/
@app.get("/items")
def get_items():
    return {"items":items}
frontend_path = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")


