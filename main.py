from fastapi import FastAPI

from app.backend.db import Base , engine
from app.models import task , user

app = FastAPI()


@app.get("/")
async def wellcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
