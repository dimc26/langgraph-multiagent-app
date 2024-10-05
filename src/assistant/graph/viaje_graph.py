from typing import Any

from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.namespace.enum import ViajeNode
from assistant.tools.viaje import ViajeState, book_node, flights_node, packagin_node, parser_viaje_node


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
