from typing import Any, TypedDict

from assistant import config as cfg
from assistant.namespace.enum import Prompt
from assistant.namespace.model import MailItem
from assistant.prompts import build_decider_prompt
from langchain_core.runnables import RunnableSerializable
from langchain_openai import ChatOpenAI


class CorreoState(TypedDict):
    mail_input: str
    mail: MailItem
    mail_message: str
    mail_output: str


def build_mail_chain() -> RunnableSerializable:
    prompt = build_decider_prompt(Prompt.MAIL.value)
    model = ChatOpenAI(
        model=cfg.PARSER_MODEL,
    ).with_structured_output(MailItem)

    return prompt | model


def parser_mail_node(state: CorreoState) -> dict[str, Any]:
    mail_chain = build_mail_chain()
    user_input = state["mail_input"]
    res = mail_chain.invoke({"text": user_input})

    return {"mail": res}


def write_mail_node(state: CorreoState) -> dict[str, str]:
    # TODO: invoke a model to write an email from the input message
    return {
        "mail_message": f"Este es un correo escrito a partir del mensaje {state['mail'].message}"
    }


def send_mail_node(state: CorreoState) -> dict[str, str]:
    # TODO: develop mail api component
    return {
        "mail_output": f"Le he mandado un correo a {state['mail'].receiver} con el siguiente mensaje {state['mail_message']}"
    }
