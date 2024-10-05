from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import CalendarItem, DeciderOptions, MailItem, QuestionItem, TravelItem
from assistant.prompts import build_decider_prompt
from assistant.utils.speech_to_text import parse_voice
from assistant.utils.text_to_speech import play_audio
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class GraphState(TypedDict):
    decider: DeciderOptions
    recognized: bool
    user_input: str
    packaging_output: str
    flights_output: str
    book_output: str
    calendar_output: str
    mail_output: str
    question_output: str


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
    play_audio("Dame un momento que gestiono tu petición")
    decider_chain = build_decider_chain()
    res = decider_chain.invoke({"text": text})

    return {"decider": res, "recognized": True, "user_input": text}
