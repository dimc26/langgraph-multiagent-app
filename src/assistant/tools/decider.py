from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import DeciderOptions
from assistant.prompts import build_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class GraphState(TypedDict):
    decider: DeciderOptions
    user_input: str
    packaging_output: str
    flights_output: str
    book_output: str
    calendar_output: str
    mail_output: str
    question_output: str


def build_decider_chain() -> RunnableSerializable:
    prompt = build_prompt(Prompt.DECIDER.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(DeciderOptions)

    return prompt | model


def decider_node(state: GraphState) -> dict[str, Any]:
    text = state["user_input"]
    decider_chain = build_decider_chain()
    res = decider_chain.invoke({"text": text})

    return {"decider": res}
