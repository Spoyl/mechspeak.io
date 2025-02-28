from fastapi import FastAPI

app = FastAPI()


@app.get("{user}/calendar/{date}")
async def read_schedule(user: str, date: str):
    return {"date":date}