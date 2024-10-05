from langgraph.graph import END, START, StateGraph
from langgraph.graph.graph import CompiledGraph

from assistant.namespace.enum import QuestionNode
from assistant.tools.question import PreguntaState, parser_question_node, search_answer_node


def build_question_graph() -> CompiledGraph:
    graph_builder = StateGraph(PreguntaState)
    graph_builder.add_node(QuestionNode.PARSER.value, parser_question_node)
    graph_builder.add_node(QuestionNode.SEARCH.value, search_answer_node)
    graph_builder.add_edge(START, QuestionNode.PARSER.value)
    graph_builder.add_edge(QuestionNode.PARSER.value, QuestionNode.SEARCH.value)
    graph_builder.add_edge(QuestionNode.SEARCH.value, END)

    return graph_builder.compile()
