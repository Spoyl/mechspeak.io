from fastapi import FastAPI
from datetime import date
from models import Booking, Timezones


CURRENT_DATE = date.isoformat(date.today())

app = FastAPI()


@app.get("/calendar/")
def read_day_itinerary(date: str=CURRENT_DATE, tmz: Timezones | None = None):
    return {"date":date, "tmz":tmz}

@app.post("/booking/")
async def make_booking(booking: Booking):
    return booking