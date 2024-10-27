from typing import Any

from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.namespace.enum import TravelNode
from assistant.tools.travel import TravelState, book_node, flights_node, packagin_node, parser_travel_node


def route_travel_nodes(state: TravelState) -> Any:
    messages = []

    for node in [TravelNode.PACKING.value, TravelNode.FLIGHTS.value]:
        message = Send(
            node=node,
            arg=state,
        )
        messages.append(message)

    return messages


def build_travel_graph() -> CompiledGraph:
    graph_builder = StateGraph(TravelState)
    graph_builder.add_node(TravelNode.PARSER.value, parser_travel_node)
    graph_builder.add_node(TravelNode.FLIGHTS.value, flights_node)
    graph_builder.add_node(TravelNode.PACKING.value, packagin_node)
    graph_builder.add_edge(START, TravelNode.PARSER.value)
    graph_builder.add_conditional_edges(
        TravelNode.PARSER.value,
        route_travel_nodes,
        [
            TravelNode.FLIGHTS.value,
            TravelNode.PACKING.value,
        ],
    )
    graph_builder.add_node(TravelNode.BOOK.value, book_node)

    graph_builder.add_edge(TravelNode.FLIGHTS.value, TravelNode.BOOK.value)
    graph_builder.add_edge(TravelNode.BOOK.value, END)
    graph_builder.add_edge(TravelNode.PACKING.value, END)

    return graph_builder.compile()
