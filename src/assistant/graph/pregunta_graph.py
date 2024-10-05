from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import Graph
from assistant.tools.pregunta import PreguntaState, parser_pregunta_node


def build_pregunta_graph() -> CompiledGraph:
    graph_builder = StateGraph(PreguntaState)
    graph_builder.add_node(Graph.PREGUNTA.value, parser_pregunta_node)
    graph_builder.add_edge(START, Graph.PREGUNTA.value)
    graph_builder.add_edge(Graph.PREGUNTA.value, END)

    return graph_builder.compile()
