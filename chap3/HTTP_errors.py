from fastapi import FastAPI, status, HTTPException
from request_body2 import InsertCar 
import datetime

app = FastAPI()

@app.post("/carsmodel")
async def new_car_model(car:InsertCar):
    if car.year > datetime.datetime.now().year:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="The car doesn't exist yet!")
    return {
        "message": car.dict()
    }
