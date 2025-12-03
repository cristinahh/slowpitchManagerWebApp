from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
async def hello():
    return ["Hello World"]
    
@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
		return{"item": item_id, "q": q}		