from fastapi import FastAPI
from enum import Enum

class Cristy(str, Enum):
    cristy = "GOAT"
    daisy = "Beautiful"

app = FastAPI()

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
@app.get("/users/{user_name}")
async def read_users(user_name : Cristy):
    if user_name is Cristy.cristy:
        return {"user_name": user_name, "message": "What happened?"}
    if user_name.value == "Beautiful":
        return {"user_name": user_name, "message": "OK then."}


