from enum import Enum
from fastapi import FastAPI


class someName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name :someName):
    if model_name is someName.alexnet:
        return{"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "resnet":
        return{"model_name": model_name, "message": "Deep Learning FTW!"}
    return{"model_name": model_name, "message" : "Whatever who cares?"}