# “ POST requests to create new resources, PUT and PATCH to update resources, and the DELETE method to delete.”

# Response and request body: 
# - request body - data that's sent from client to our API 



from fastapi import FastAPI, Body

app = FastAPI()

# this endpoint would be usd to insert new cars into our future databases
@app.post("/cars")
async def new_car(data: dict=Body(...)):
    print(data)
    return {
        "message": data
    }

@app.get("/cars")
async def new_car(data: dict=Body(...)):
    print(data)
    return {
        "message": data
    }
# Body
# Path
# Query 