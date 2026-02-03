from fastapi import APIRouter

router = APIRouter()

items = []

@router.get("/lostfound")
def get_items():
    return items

@router.post("/lostfound")
def add_item(data: dict):
    items.append(data["item"])
    return {"message": "Item added"}
