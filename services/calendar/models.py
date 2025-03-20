from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID
from datetime import datetime
from sqlmodel import SQLModel, Field


class Booking(SQLModel, table=True):
    lesson_id: UUID | None = Field(primary_key=True, default=None)
    start: datetime = Field(index=True, examples=["2025-03-09T07:28:12.955Z"])
    dur: int = Field(default= 50, description="A value of '50' is a lesson, '25' is a trial")
    paid: bool
    who: list[str] = set()


class Timezones(str, Enum):
    GMT= "GMT"
    Bali= "Bali"
    France= "France"


class Lesson(BaseModel):
    lesson_id: UUID
    start: datetime = Field(examples=["2025-03-09T07:28:12.955Z"])
    dur: int = Field(default= 50, description="Duration defines whether the lesson is a trial or not")
    paid: bool
    who: list[str] = set()

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "lesson_id": "550e8400-e29b-41d4-a716-446655440000",
                    "description": "2025-03-09T07:28:12.955Z",
                    "dur": 25,
                    "paid": True,
                    "who": [
                        "foo@bar.com",
                        "example_user@email.com"
                    ]
                }
            ]
        }
    }
