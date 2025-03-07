from fastapi import FastAPI, Query
from datetime import date
from models import Lesson, Timezones
from typing import Annotated


CURRENT_DATE = date.isoformat(date.today())

app = FastAPI()


@app.get("/calendar/")
def read_day_itinerary(date: Annotated[str | None, Query(title="Requested Date", pattern = "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")] = CURRENT_DATE, 
                       tmz: Timezones | None = Timezones.GMT):
    return {"date":date, "tmz":tmz}

@app.post("/booking/")
async def make_booking(booking: Lesson):
    Lesson.lesson_id = Lesson.dat + "_" + Lesson.start + "_" + Lesson.dur
    return booking