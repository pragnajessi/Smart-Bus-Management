from fastapi import FastAPI
from routes import announcements
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# 🔊 ANNOUNCEMENTS + WAKEUP
# -------------------------------

current_stop = ""

class StopUpdate(BaseModel):
    stop: str

@app.post("/update-stop")
def update_stop(data: StopUpdate):
    global current_stop
    current_stop = data.stop
    return {"status": "updated", "current_stop": current_stop}

@app.get("/announcements")
def get_announcements():
    return {"current_stop": current_stop}
app.include_router(announcements.router, prefix="/announcements")

# -------------------------------
# 💺 SEAT RESERVATION
# -------------------------------

class Seat(BaseModel):
    seat_no: int
    name: str

reserved_seats: List[Seat] = []

@app.post("/reserve-seat")
def reserve_seat(seat: Seat):
    for s in reserved_seats:
        if s.seat_no == seat.seat_no:
            return {"error": "Seat already booked"}

    reserved_seats.append(seat)
    return {"message": "Seat booked", "seats": reserved_seats}

@app.get("/seats")
def get_seats():
    return reserved_seats


# -------------------------------
# 🎒 LOST & FOUND
# -------------------------------

class Item(BaseModel):
    item: str
    location: str
    contact: str

lost_items: List[Item] = []

@app.post("/lostfound")
def report_item(item: Item):
    lost_items.append(item)
    return {"message": "Reported successfully"}

@app.get("/lostfound")
def get_items():
    return lost_items


# -------------------------------
# 🧪 HEALTH CHECK
# -------------------------------

@app.get("/")
def home():
    return {
        "status": "Smart Bus System Backend Running",
        "modules": [
            "Voice Announcements",
            "Wakeup Alert",
            "Seat Reservation",
            "Lost and Found"
        ]
    }
