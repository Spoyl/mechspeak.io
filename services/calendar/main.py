from fastapi import FastAPI, Query, Path, status, Depends
from datetime import date
from models import Lesson, Timezones, Booking
from typing import Annotated
from sqlmodel import create_engine, select, SQLModel, Session


CURRENT_DATE = date.isoformat(date.today())

# db params:
sqlite_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tabulate():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session())]


app = FastAPI()


@app.get("/lessons/")
def request_itin(
    date: Annotated[str | None, Query(pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")] = CURRENT_DATE, 
    tmz: Timezones | None = Timezones.GMT):
    """
    Request method. Retrieves schedule information from the db. 
    """
    return {"date":date, "tmz":tmz}


@app.post("/lessons/", status_code=status.HTTP_201_CREATED)
async def make_booking(booking: Lesson):
    """
    Post method. Creates a new entry in the calendar db.
    """
    lesson_dict = booking.model_dump()
    Lesson.lesson_id = lesson_dict["dat"] + "_" + lesson_dict["start"] + "_" + str(lesson_dict["dur"])
    return {"lesson_id": Lesson.lesson_id}


@app.get("/lessons/{lesson_id}")
async def lesson_info(lesson_id: Annotated[str, Path(title = "Unique lesson identifier")]):
    """
    Request method. Retrieves information about a specific lesson from the server.
    """
    results = {"lesson_id" : lesson_id}
    return results


@app.put("/lessons/{lesson_id}")
async def update_info(lesson_id: Annotated[str, Path(title = "Unique lesson identifier")],
                      reschedule: bool | None = None,
                      cancel: bool | None = None):
    """
    Method for updating an event in the calendar.
    """
    if cancel:
        result = "Cancel Lesson " + str(lesson_id)
    else:
        result = reschedule.model_dump()

    return result


@app.delete("/lessons/{lesson_id}")
async def cancel(lesson_id: Annotated[str, Path(title = "Unique lesson identifier")]):
    """
    Method to delete an event in the calendar.
    """
    return None