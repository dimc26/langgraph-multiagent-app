from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CalendarItem
from assistant.prompts import build_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class CalendarioState(TypedDict):
    calendar_input: str
    calendar: CalendarItem
    calendar_output: str


def build_calendar_chain() -> RunnableSerializable:
    prompt = build_prompt(Prompt.CALENDAR.value)
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
    formatted_string = cfg.LANGUAGE_MSG["calendar_output"][cfg.MSG_SELECTED_LANGUAGE].format(
        day=state["calendar"].day,
        hour=state["calendar"].hour
    )
    return { "calendar_output": formatted_string}
