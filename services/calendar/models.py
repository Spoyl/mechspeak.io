from pydantic import BaseModel
from enum import Enum
from datetime import date



class Timezones(str, Enum):
    GMT = "GMT"
    Bali = "Bali"
    France = "France"


class Lesson(BaseModel):
    dat: str
    start: str
    dur: int
    paid: bool
    who: str | None = None
    lesson_id: str