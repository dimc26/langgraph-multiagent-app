from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import QuestionItem
from assistant.prompts import build_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI
from tavily import TavilyClient


class PreguntaState(TypedDict):
    question_input: str
    question: QuestionItem
    question_output: str


def build_question_chain() -> RunnableSerializable:
    prompt = build_prompt(Prompt.QUESTION.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(QuestionItem)

    return prompt | model


def parser_question_node(state: PreguntaState) -> dict[str, Any]:
    question_chain = build_question_chain()
    user_input = state["question_input"]
    res = question_chain.invoke({"text": user_input})

    return {"question": res}


def search_answer_node(state: PreguntaState) -> dict[str, Any]:
    question = state["question"].text
    tavily_client = TavilyClient(api_key=cfg.TAVILY_API_KEY)
    res = tavily_client.qna_search(question)

    return {"question_output": res}
