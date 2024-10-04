from typing import TypedDict

from assistant.namespace.model import CorreoItem


class CorreoState(TypedDict):
    user_input: str
    correo: CorreoItem


def pregunta_node(state: CorreoState) -> None:
    print("Llego aquí PREGUNTA")
