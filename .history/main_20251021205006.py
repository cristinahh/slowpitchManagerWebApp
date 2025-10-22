from fastapi import FastAPI

app = await FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}