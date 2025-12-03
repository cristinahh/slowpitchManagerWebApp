from fastapi import FastAPI
from enum import Enum

class SomeClass(str, Enum):
    thing1 = "one"
    thing2 = "two"
    thing3 = "three"

app = FastAPI()

@app.get("/some/{name}")
async def get_name(name: SomeClass):
    if SomeClass.name = "one"

