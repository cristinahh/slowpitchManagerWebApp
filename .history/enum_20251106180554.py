from fastapi import FastAPI
from enum import Enum

class SomeClass(int, Enum):
    thing1 = 1
    thing2 = 2
    thing3 = 3

app = FastAPI()

@app.get("/some/{name}")
async def get_name(name: SomeClass):
    if name is SomeClass.thing1:
        return {"name": name, "message": "Thing 1"}
    if name.value == "two":
        return {"name": name, "message": "Thing 2"}
    return { "name": name, "message": "Thing 3"}
