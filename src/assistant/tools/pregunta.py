from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import PreguntaItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class PreguntaState(TypedDict):
    pregunta_input: str
    pregunta: PreguntaItem


def build_pregunta_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.PREGUNTA.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(PreguntaItem)

    return prompt | model


def parser_pregunta_node(state: PreguntaState) -> dict[str, Any]:
    pregunta_chain = build_pregunta_chain()
    user_input = state["pregunta_input"]
    res = pregunta_chain.invoke({"text": user_input})
    print(res)

    return {"pregunta": res}
