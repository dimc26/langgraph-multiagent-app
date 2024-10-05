from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import Graph
from assistant.tools.correo import CorreoState, parser_correo_node


def build_correo_graph() -> CompiledGraph:
    graph_builder = StateGraph(CorreoState)
    graph_builder.add_node(Graph.CORREO.value, parser_correo_node)
    graph_builder.add_edge(START, Graph.CORREO.value)
    graph_builder.add_edge(Graph.CORREO.value, END)

    return graph_builder.compile()
