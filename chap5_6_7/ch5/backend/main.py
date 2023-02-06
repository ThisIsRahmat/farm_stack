from fastapi import fastAPI
from fastapi import APIRouter, Body, request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models import CarBase


from routers.cars import router as cars_router

app = fastAPI

origins = [
	"http://localhost",
	"http://localhost:8080",
	"http://localhost:3000",
	"http://localhost:8000"
]

app.include_routers(cars_router, prefix="/cars", tags=["cars"])

