from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
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
#Run Command: http://0.0.0.0:8000/
#Frontend: 5500 | Backend:8000
@app.get("/items")
def get_items():
    return items

app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")
@app.get("/")
def read_root():
    return FileResponse("../frontend")
