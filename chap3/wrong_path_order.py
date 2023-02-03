from fastapi import FastAPI

app = FastAPI()



#This failes because you need to start with the static path before the dynamic path 

@app.get("/user/{id}")
async def user(id:int):
    return {"User_id": id}

@app.get("/user/me")
async def user():
    return {"User_id": "This is me!"}

