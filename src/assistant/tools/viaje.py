from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import ViajeItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class ViajeState(TypedDict):
    user_input: str
    viaje: ViajeItem
    packaging: str
    flights: str
    book: str


def build_viaje_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.PREGUNTA.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(ViajeItem)

    return prompt | model


def parser_viaje_node(state: ViajeState) -> dict[str, Any]:
    viaje_chain = build_viaje_chain()
    user_input = state["user_input"]
    res = viaje_chain.invoke({"text": user_input})
    print(res)

    return {"viaje": res}


def flights_node(state: ViajeState) -> dict[str, str]:
    print("vuelo")
    return {"flights": "Vuelo 9822Y"}


def book_node(state: ViajeState) -> dict[str, str]:
    print("book")
    return {"book": "Hotel Palace"}


def packagin_node(state: ViajeState) -> dict[str, str]:
    print("maleta")
    return {"packaging": "Te aconsejo llevar una rebequita"}
