from fastapi import APIRouter

router = APIRouter()

seats = [0] * 20   # 20 seats

@router.get("/seats")
def get_seats():
    return seats

@router.post("/reserve")
def reserve(data: dict):
    seat = data["seat"]
    seats[seat] = 1
    return {"message": "Seat reserved"}
