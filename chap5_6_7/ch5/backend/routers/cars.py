
from fastapi import APIRouter

router = APIRouter()

@router.get("/" response_description="List all cars")
async def list_cars():
	return {"data": "All cars will go here"}
	
	
@router.post("/", response_description="Add new car")
async def create_car(request: request, car: CarBase = Body(...)):
	car = jsonable_encoder(car)
	new_car = await request.app.mongodb[cars].insert_one(car)
	created_car = await request.app.mongodb["cars".fin_one({"_id": new_car.inserted_id})]
	
	return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_car
		

@router.get("/{id}", response_description="Get a single car")
async def show_car(id: str, request: Request):
	if (car := await request.app.mongodb["cars"].find_one({"_id": id})) is not None:
		return CarDB(**car)
	raise HTTPException(status_code=404, detail=f"Car with {id}not found")
	

@router.get("/", response_description="List all cars")
async def list_all_cars( request: request, min_price: int=0, max_price: int=100000, brand: Optional[str]=None, page: int=1) -> List[CarDB]:
	RESULTS_PER_PAGE = 25
	skip = (page-1)*RESULTS_PER_PAGE
	query = { "price": {"$lt": max_price, "$gt":min_price}}
	if brand:
		query["brand"] = brand
		full_query = request.app.mongodb['cars'].find(query).sort('_id', 1).skip(skip).limit(RESULTS_PER_PAGE)
		results = [CarDB(**raw_car) async for raw_car in full_query]
		return results
		
		
@router.patch("/{id}", response_description="Update car")
async def update_task(id: str, request: Request, car: CarUpdate = Body(...)):
	await request.app.mongodb[car].update_one(
		{"_id": id}, {'$ser': car.dict(exclude_unset=True)})
		if (car := await request.app.mongodb['cars'])
		
		
@router.delete("/{id}", response_description="Delete car")
async def delete_task(id: str, request: Request):
	delete_result = await request.app.mongodb['cars'].delete_one({"_id": id})
	if delete_result.deleted_Count == 1:
		return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
		raise HTTPException(status_code=404, detail=f"Car with{id} not found")
		
		
		
		
		
		
		
		
		
		
		