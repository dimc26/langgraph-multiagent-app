from typing import Any, TypedDict

from langgraph.constants import END
from langgraph.graph import START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.chains.decider import build_decider_chain
from assistant.graph.calendario import calendario_node
from assistant.graph.correo import correo_node
from assistant.graph.pregunta import pregunta_node
from assistant.graph.viaje import build_viaje_graph
from assistant.namespace.enum import Graph, Node
from assistant.namespace.model import DeciderOptions
from assistant.utils.speech_to_text import parse_voice
from assistant.utils.text_to_speech import play_answer

decider_chain = build_decider_chain()
viaje_graph = build_viaje_graph()

class GraphState(TypedDict):
    decider: DeciderOptions
    recognized: bool
    user_input: str


def decider_node(state: GraphState) -> dict[str, Any]:
    recognized, text = parse_voice()
    if not recognized:
        return {"recognized": False}
    play_answer("Dame un momento que gestiono tu petición")
    res = decider_chain.invoke({"text": text})
    print(res)

    return {"decider": res, "recognized": True, "user_input": text}


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
                send_state = {
                    "user_input": user_input
                }

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
        [Node.CORREO.value, Node.CALENDARIO.value, Graph.VIAJE.value, Node.PREGUNTA.value, END],
    )

    graph_builder.add_node(Node.CORREO.value, correo_node)
    graph_builder.add_node(Node.CALENDARIO.value, calendario_node)
    graph_builder.add_node(Graph.VIAJE.value, viaje_graph)
    graph_builder.add_node(Node.PREGUNTA.value, pregunta_node)

    graph_builder.add_edge(Node.CORREO.value, END)
    graph_builder.add_edge(Node.CALENDARIO.value, END)
    graph_builder.add_edge(Graph.VIAJE.value, END)
    graph_builder.add_edge(Node.PREGUNTA.value, END)

    return graph_builder.compile()
