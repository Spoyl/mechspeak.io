from pydantic import BaseModel
from enum import Enum


class Timezones(str, Enum):
    GMT = "GMT"
    Bali = "Bali"
    France = "France"

class Booking(BaseModel):
    date: str
    start_time: str
    length: int
    teacher: str