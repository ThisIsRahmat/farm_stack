

from fastapi import FastAPI, Request
app = FastAPI()
@app.get("/cars2")
async def raw_request(request:Request):return{
    "message": request.base_url,
    "all":dir(request)
}



# Request bodies,
# Query strings,
# Paths