
from typing import Any

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.prompts import load_prompt_by_name
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


def build_prompt(prompt: str) -> ChatPromptTemplate:
    human_msg_prompt = load_prompt_by_name(f"{prompt}_human")

    return ChatPromptTemplate(
        [HumanMessagePromptTemplate.from_template(human_msg_prompt)],
        input_variables=["text"],
    )


def build_format_answer_chain() -> RunnableSerializable:
    prompt = build_prompt(Prompt.FORMAT_ANSWER.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    )

    return prompt | model


def format_answer(answer: dict[str, Any] | Any) -> Any:
    format_answer_chain = build_format_answer_chain()
    res = format_answer_chain.invoke({"text": answer})

    return res
