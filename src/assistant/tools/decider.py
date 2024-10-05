from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CalendarioItem, CorreoItem, DeciderOptions, PreguntaItem, ViajeItem
from assistant.prompts import build_decider_prompt
from assistant.utils.speech_to_text import parse_voice
from assistant.utils.text_to_speech import play_answer
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class GraphState(TypedDict):
    decider: DeciderOptions
    recognized: bool
    user_input: str
    viaje: ViajeItem
    calendario: CalendarioItem
    correo: CorreoItem
    pregunta: PreguntaItem


def build_decider_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.DECIDER.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(DeciderOptions)

    return prompt | model


def decider_node(state: GraphState) -> dict[str, Any]:
    recognized, text = parse_voice()
    if not recognized:
        return {"recognized": False}
    play_answer("Dame un momento que gestiono tu petición")
    decider_chain = build_decider_chain()
    res = decider_chain.invoke({"text": text})
    print(res)

    return {"decider": res, "recognized": True, "user_input": text}
