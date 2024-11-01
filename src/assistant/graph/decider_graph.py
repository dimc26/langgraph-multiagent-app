from typing import Any

from langgraph.constants import END
from langgraph.graph import START, StateGraph
from langgraph.graph.graph import CompiledGraph, Send

from assistant.graph.calendar_graph import build_calendar_graph
from assistant.graph.mail_graph import build_mail_graph
from assistant.graph.question_graph import build_question_graph
from assistant.graph.travel_graph import build_travel_graph
from assistant.namespace.enum import Graph, Node
from assistant.tools.decider import GraphState, decider_node

travel_graph = build_travel_graph()
mail_graph = build_mail_graph()
calendar_graph = build_calendar_graph()
question_graph = build_question_graph()


def send_to_end() -> Send:
    mssg = Send(
        node=END,
        arg=None,
    )
    return mssg


def route_tasks_nodes(state: GraphState) -> Any:
    decider = state["decider"]
    user_input = state["user_input"]
    messages = []
    for field, value in decider.dict().items():
        if value:
            send_state = {f"{field}_input": user_input}

            message = Send(
                node=f"{field}_graph",
                arg=send_state,
            )
            messages.append(message)
    if not messages:
        mssg = send_to_end()
        messages.append(mssg)

    return messages


def build_assistant_graph() -> CompiledGraph:
    graph_builder = StateGraph(GraphState)
    graph_builder.add_node(Node.DECIDER.value, decider_node)
    graph_builder.add_edge(START, Node.DECIDER.value)
    graph_builder.add_conditional_edges(
        Node.DECIDER.value,
        route_tasks_nodes,
        [Graph.MAIL.value, Graph.CALENDAR.value, Graph.TRAVEL.value, Graph.QUESTION.value, END],
    )

    graph_builder.add_node(Graph.MAIL.value, mail_graph)
    graph_builder.add_node(Graph.CALENDAR.value, calendar_graph)
    graph_builder.add_node(Graph.TRAVEL.value, travel_graph)
    graph_builder.add_node(Graph.QUESTION.value, question_graph)

    graph_builder.add_edge(Graph.MAIL.value, END)
    graph_builder.add_edge(Graph.CALENDAR.value, END)
    graph_builder.add_edge(Graph.TRAVEL.value, END)
    graph_builder.add_edge(Graph.QUESTION.value, END)

    return graph_builder.compile()
