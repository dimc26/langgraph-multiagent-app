from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import Graph
from assistant.tools.calendario import CalendarioState, parser_calendario_node


def build_calendario_graph() -> CompiledGraph:
    graph_builder = StateGraph(CalendarioState)
    graph_builder.add_node(Graph.CALENDARIO.value, parser_calendario_node)
    graph_builder.add_edge(START, Graph.CALENDARIO.value)
    graph_builder.add_edge(Graph.CALENDARIO.value, END)

    return graph_builder.compile()
