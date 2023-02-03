# Pydantic - python library for data validation, catches invalid data 


# “Enum class, -  create an enumeration type for the admissible types of fuel.”


from enum import Enum
from typing import List
from pydantic import BaseModel, ValidationError
class Fuel(str, Enum):
    PETROL = 'PETROL'
    DIESEL = 'DIESEL'
    LPG = 'LPG'

class Car(BaseModel):
      brand: str
      model: str
      year: str
      fuel: str
      countries: List[str]
      note:str="No note"

car = Car(
    brand="Lancia",
    model="Musa",
    fuel="PETROL",
    year="2006",
    countries=["Italy","France"]
)
print(car.json())


# catch invalid data type

try:
    invalid_car = Car(
        brand="Lancia",
        fuel="PETROL",
        year="something",
        countries=["Italy","France"]
)
except ValidationError as e:
    print(e)


“uvicorn first_endpoint:app --reload”

Excerpt From
Full Stack FastAPI, React, and MongoDB
Marko AleksendriÄ‡
This material may be protected by copyright.