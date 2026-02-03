from fastapi import APIRouter

router = APIRouter()

alerts = []

@router.post("/update-stop")
def update_stop(data: dict):
    alerts.append(data["stop"])
    return {"message": "Wake alert sent"}

@router.get("/alerts")
def get_alerts():
    return {"alerts": alerts}
