from fastapi import APIRouter

router = APIRouter()

bus_stops = [
    "Vijayawada",
    "Guntur",
    "Tenali",
    "Ongole",
    "Nellore",
    "Tirupati"
]

current_stop = ""

@router.get("/stops")
def get_stops():
    return bus_stops

@router.post("/announce")
def announce(data: dict):
    global current_stop
    current_stop = data["stop"]
    return {"message": f"Announcing {current_stop}"}
