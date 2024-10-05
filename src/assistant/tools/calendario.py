from typing import Any, TypedDict

from assistant import config as cfg

# from assistant.graph.calendario_graph import CalendarioState
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CalendarioItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class CalendarioState(TypedDict):
    calendario_input: str
    calendario: CalendarioItem


def build_calendario_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.CALENDARIO.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(CalendarioItem)

    return prompt | model


def parser_calendario_node(state: CalendarioState) -> dict[str, Any]:
    calendario_chain = build_calendario_chain()
    user_input = state["calendario_input"]
    res = calendario_chain.invoke({"text": user_input})
    print(res)

    return {"calendario": res}
