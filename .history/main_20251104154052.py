from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty", "Cristy"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]