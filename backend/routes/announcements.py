from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

stops = []   # ONE shared list

class Stop(BaseModel):
    stop: str

@router.post("/add")
def add_stop(data: Stop):
    stops.append(data.stop)
    return {"message": "Stop added"}

@router.get("/")
def get_stops():
    return stops

@router.delete("/clear")
def clear_stops():
    stops.clear()
    return {"message": "Cleared"}
