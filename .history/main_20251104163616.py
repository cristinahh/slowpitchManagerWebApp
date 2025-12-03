from fastapi import FastAPI
from enum import Enum

class SomeClass(str, Enum):
    thing1 = "one"
    thing2 = "two"
    thing3 = "three"

app = FastAPI()

@app.get("/some/{name}")
async def get_name(name: SomeClass):
    if name is SomeClass.thing1:
        return {"name": name, "message": "Thing 1"}
    if name.value == "two":
        return {"name": name, "message": "Thing 2"}

