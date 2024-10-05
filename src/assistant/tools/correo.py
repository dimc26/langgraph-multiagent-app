from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CorreoItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class CorreoState(TypedDict):
    correo_input: str
    correo: CorreoItem


def build_correo_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.CORREO.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(CorreoItem)

    return prompt | model


def parser_correo_node(state: CorreoState) -> dict[str, Any]:
    correo_chain = build_correo_chain()
    user_input = state["correo_input"]
    res = correo_chain.invoke({"text": user_input})
    print(res)

    return {"correo": res}
