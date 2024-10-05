from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import TravelItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class ViajeState(TypedDict):
    travel_input: str
    travel: TravelItem
    packaging_output: str
    flights_output: str
    book_output: str


def build_travel_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.TRAVEL.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(TravelItem)

    return prompt | model


def parser_travel_node(state: ViajeState) -> dict[str, Any]:
    travel_chain = build_travel_chain()
    user_input = state["travel_input"]
    res = travel_chain.invoke({"text": user_input})

    return {"travel": res}


def flights_node(state: ViajeState) -> dict[str, str]:
    # TODO: develop the api component to recommend flights if the date is not specific or to buy tickets if it is an exact date
    return {"flights_output": f"Vuelo Syntonize con destino {state['travel'].destination} para {state['travel'].date}"}


def book_node(state: ViajeState) -> dict[str, str]:
    # TODO: develop the api component to recommend hotels if the date is not specific or to buy book a room if it is exact date
    return {"book_output": f"Reservado hotel Syntonize en {state['travel'].destination} para {state['travel'].date}"}


def packagin_node(state: ViajeState) -> dict[str, str]:
    # TODO: invoke a model to get advice on clothing in view of the weather
    return {
        "packaging_output": f"Llévate una rebequita a {state['travel'].destination} que refresca en {state['travel'].date}"
    }
