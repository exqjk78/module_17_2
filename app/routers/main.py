from fastapi import FastAPI
from routers import tasks
from routers import user

app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}