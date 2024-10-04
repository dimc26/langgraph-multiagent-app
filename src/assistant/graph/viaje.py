from typing import Any, TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.namespace.enum import ViajeNode
from assistant.namespace.model import ViajeItem


class ViajeState(TypedDict):
    user_input: str
    viaje: ViajeItem
    packaging: str
    flights: str
    book: str


def parser_viaje_node(state: ViajeState) -> ViajeState:
    print("viaje")
    return state

def flights_node(state: ViajeState) -> dict[str, str]:
    print("vuelo")
    return {"flights": "Vuelo 9822Y"}

def book_node(state: ViajeState) -> dict[str, str]:
    print("book")
    return {"book": "Hotel Palace"}

def packagin_node(state: ViajeState) -> dict[str, str]:
    print("maleta")
    return {"packaging": "Te aconsejo llevar una rebequita"}

def route_pages(state: ViajeState) -> Any:
    messages = []

    for node in [ViajeNode.PACKING.value, ViajeNode.FLIGHTS.value]:
        message = Send(
            node=node,
            arg=state,
        )
        messages.append(message)

    return messages


def build_viaje_graph() -> CompiledGraph:
    graph_builder = StateGraph(ViajeState)
    graph_builder.add_node(ViajeNode.PARSER.value, parser_viaje_node)
    graph_builder.add_node(ViajeNode.FLIGHTS.value, flights_node)
    graph_builder.add_node(ViajeNode.PACKING.value, packagin_node)
    graph_builder.add_edge(START, ViajeNode.PARSER.value)
    graph_builder.add_conditional_edges(
            ViajeNode.PARSER.value,
            route_pages,
            [
                ViajeNode.FLIGHTS.value,
                ViajeNode.PACKING.value,
            ],
        )
    graph_builder.add_node(ViajeNode.BOOK.value, book_node)

    graph_builder.add_edge(ViajeNode.FLIGHTS.value, ViajeNode.BOOK.value)
    graph_builder.add_edge(ViajeNode.BOOK.value, END)
    graph_builder.add_edge(ViajeNode.PACKING.value, END)

    return graph_builder.compile()
