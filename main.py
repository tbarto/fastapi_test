from fastapi import FastAPI
from models.message import Msg

# Define an API object
app = FastAPI()

# Map HTTP method and path to python function
@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to the API home page!"}


@app.get("/path")
async def function_demo_get():
    return {"message": "This is /path endpoint, use post request to transform text to uppercase"}


@app.post("/path")
async def function_demo_post(inp: Msg):
    return {"message": inp.msg.upper()}

@app.post("/lower")
async def function_demo_post(inp: Msg):
    return {"message": inp.msg.lower()}

@app.get("/path/{path_id}")
async def function_demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}

