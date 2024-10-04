from typing import TypedDict

from assistant.namespace.model import CalendarioItem


class CalendarioState(TypedDict):
    user_input: str
    calendario: CalendarioItem


def calendario_node(state: CalendarioState) -> None:
    print("Llego aquí CALENDARIO")
