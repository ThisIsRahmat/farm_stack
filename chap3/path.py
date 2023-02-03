from fastapi import FastAPI
app = FastAPI()


@app.get("/car/{id}")
# same route without the type hinting to make sure the id is only integer
async def root(id):
    return {"car_id": id}

@app.get("/carh/{id}")
# Adding type (id: int) hinting to make sure the id is only integer
async def root(id:int):
    return {"car_id": id}