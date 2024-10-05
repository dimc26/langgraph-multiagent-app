from typing import Any

from langgraph.constants import END
from langgraph.graph import START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.graph.calendario_graph import build_calendario_graph
from assistant.graph.correo_graph import build_correo_graph
from assistant.graph.pregunta_graph import build_pregunta_graph
from assistant.graph.viaje_graph import build_viaje_graph
from assistant.namespace.enum import Graph, Node
from assistant.tools.decider import GraphState, decider_node

viaje_graph = build_viaje_graph()
correo_graph = build_correo_graph()
calendario_graph = build_calendario_graph()
pregunta_graph = build_pregunta_graph()


def route_pages(state: GraphState) -> Any:
    decider = state["decider"]
    recognized = state["recognized"]
    user_input = state["user_input"]
    messages = []
    if not recognized:
        message = Send(
            node=END,
            arg=None,
        )
    else:
        for field, value in decider.dict().items():
            if value:
                send_state = {f"{field}_input": user_input}

                message = Send(
                    node=f"{field}_node",
                    arg=send_state,
                )
                messages.append(message)

    return messages


def build_assistant_graph() -> CompiledGraph:
    graph_builder = StateGraph(GraphState)
    graph_builder.add_node(Node.DECIDER.value, decider_node)
    graph_builder.add_edge(START, Node.DECIDER.value)
    graph_builder.add_conditional_edges(
        Node.DECIDER.value,
        route_pages,
        [Graph.CORREO.value, Graph.CALENDARIO.value, Graph.VIAJE.value, Graph.PREGUNTA.value, END],
    )

    graph_builder.add_node(Graph.CORREO.value, correo_graph)
    graph_builder.add_node(Graph.CALENDARIO.value, calendario_graph)
    graph_builder.add_node(Graph.VIAJE.value, viaje_graph)
    graph_builder.add_node(Graph.PREGUNTA.value, pregunta_graph)

    graph_builder.add_edge(Graph.CORREO.value, END)
    graph_builder.add_edge(Graph.CALENDARIO.value, END)
    graph_builder.add_edge(Graph.VIAJE.value, END)
    graph_builder.add_edge(Graph.PREGUNTA.value, END)

    return graph_builder.compile()
