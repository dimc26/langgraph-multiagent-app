from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CalendarItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class CalendarioState(TypedDict):
    calendar_input: str
    calendar: CalendarItem
    calendar_output: str


def build_calendar_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.CALENDAR.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(CalendarItem)

    return prompt | model


def parser_calendar_node(state: CalendarioState) -> dict[str, Any]:
    calendar_chain = build_calendar_chain()
    user_input = state["calendar_input"]
    res = calendar_chain.invoke({"text": user_input})

    return {"calendar": res}

def set_event_node(state: CalendarioState) -> dict[str, str]:
    # TODO: invoke a model to get advice on clothing in view of the weather
    return {
        "calendar_output": f"He creado un evento para el día {state['calendar'].day} a las {state['calendar'].hour}"
    }
