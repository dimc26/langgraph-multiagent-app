from datetime import time
from typing import Optional as Opt

from langchain_core.pydantic_v1 import BaseModel


class MailItem(BaseModel):
    receiver: str
    message: str


class CalendarItem(BaseModel):
    day: str
    hour: Opt[time]


class TravelItem(BaseModel):
    destination: str
    date: str


class QuestionItem(BaseModel):
    text: str


class DeciderOptions(BaseModel):
    mail: bool
    calendar: bool
    travel: bool
    question: bool
