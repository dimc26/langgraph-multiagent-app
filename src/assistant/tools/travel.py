from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import TravelItem
from assistant.prompts import build_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class TravelState(TypedDict):
    travel_input: str
    travel: TravelItem
    packaging_output: str
    flights_output: str
    book_output: str


def build_travel_chain() -> RunnableSerializable:
    prompt = build_prompt(Prompt.TRAVEL.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(TravelItem)

    return prompt | model


def parser_travel_node(state: TravelState) -> dict[str, Any]:
    travel_chain = build_travel_chain()
    user_input = state["travel_input"]
    res = travel_chain.invoke({"text": user_input})

    return {"travel": res}


def flights_node(state: TravelState) -> dict[str, str]:
    # TODO: develop the api component to recommend flights if the date is not specific or to buy tickets if exact date
    formatted_string = cfg.LANGUAGE_MSG["flights_output"][cfg.MSG_SELECTED_LANGUAGE].format(
        destination=state["travel"].destination,
        date=state["travel"].date
    )
    return {"flights_output": formatted_string}


def book_node(state: TravelState) -> dict[str, str]:
    # TODO: develop the api component to recommend hotels if the date is not specific or to book a room if exact date
    formatted_string = cfg.LANGUAGE_MSG["book_output"][cfg.MSG_SELECTED_LANGUAGE].format(
        destination=state["travel"].destination,
        date=state["travel"].date
    )
    return {"book_output": formatted_string}


def packagin_node(state: TravelState) -> dict[str, str]:
    # TODO: invoke a model to get advice on clothing in view of the weather
    formatted_string = cfg.LANGUAGE_MSG["packaging_output"][cfg.MSG_SELECTED_LANGUAGE].format(
        destination=state["travel"].destination,
        date=state["travel"].date
    )
    return {"packaging_output": formatted_string}
