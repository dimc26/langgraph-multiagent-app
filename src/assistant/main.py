from langgraph.graph.state import CompiledGraph, RunnableConfig

from assistant.graph.decider_graph import build_assistant_graph
from assistant.tools.format_answer import format_answer


def save_results(graph: CompiledGraph) -> None:
    with open("graph.png", "wb") as f:
        f.write(graph.get_graph(xray=1).draw_mermaid_png())


def processing(user_input: str) -> str:
    graph = build_assistant_graph()
    graph_config = RunnableConfig(
        max_concurrency=4,
        recursion_limit=50,
    )
    res = graph.invoke(
        input={"user_input": user_input},
        config=graph_config,
    )
    formatted_res = format_answer(res)
    save_results(graph)

    return formatted_res.content
