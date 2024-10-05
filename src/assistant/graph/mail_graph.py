from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import MailNode
from assistant.tools.mail import CorreoState, parser_mail_node, send_mail_node, write_mail_node


def build_mail_graph() -> CompiledGraph:
    graph_builder = StateGraph(CorreoState)
    graph_builder.add_node(MailNode.PARSER.value, parser_mail_node)
    graph_builder.add_node(MailNode.WRITE.value, write_mail_node)
    graph_builder.add_node(MailNode.SEND.value, send_mail_node)
    graph_builder.add_edge(START, MailNode.PARSER.value)
    graph_builder.add_edge(MailNode.PARSER.value, MailNode.WRITE.value)
    graph_builder.add_edge(MailNode.WRITE.value, MailNode.SEND.value)
    graph_builder.add_edge(MailNode.SEND.value, END)

    return graph_builder.compile()
