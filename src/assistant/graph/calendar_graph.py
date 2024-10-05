from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import CalendarNode
from assistant.tools.calendar import CalendarioState, parser_calendar_node, set_event_node


def build_calendar_graph() -> CompiledGraph:
    graph_builder = StateGraph(CalendarioState)
    graph_builder.add_node(CalendarNode.PARSER.value, parser_calendar_node)
    graph_builder.add_node(CalendarNode.EVENT.value, set_event_node)
    graph_builder.add_edge(START, CalendarNode.PARSER.value)
    graph_builder.add_edge(CalendarNode.PARSER.value, CalendarNode.EVENT.value)
    graph_builder.add_edge(CalendarNode.EVENT.value, END)

    return graph_builder.compile()
