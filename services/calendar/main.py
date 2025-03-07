from fastapi import FastAPI, Query, Path
from datetime import date
from models import Lesson, Timezones
from typing import Annotated


CURRENT_DATE = date.isoformat(date.today())

app = FastAPI()


@app.get("/lessons/")
def read_day_itinerary(
    date: Annotated[str | None, Query(title="Requested Date", pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")] = CURRENT_DATE, 
    tmz: Annotated[Timezones | None, Path(title = "The display timezone for the calendar")] = Timezones.GMT):
    return {"date":date, "tmz":tmz}

@app.post("/lessons/")
async def make_booking(booking: Lesson):
    Lesson.lesson_id = Lesson.dat + "_" + Lesson.start + "_" + Lesson.dur
    return booking

@app.get("lessons/{lesson_id}")
async def lesson_info():
    return None

@app.put("lessons/{lesson_id}")
async def update_info():
    return None

@app.delete("lessons/{lesson_id}")
async def cancel():
    return None