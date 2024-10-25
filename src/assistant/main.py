from langgraph.graph.state import CompiledGraph, RunnableConfig

from assistant.graph.decider_graph import build_assistant_graph
from assistant.tools.format_answer import format_answer
from assistant.utils.text_to_speech import play_audio


def save_results(graph: CompiledGraph) -> None:
    with open("graph.png", "wb") as f:
        f.write(graph.get_graph(xray=1).draw_mermaid_png())


def main() -> None:
    graph = build_assistant_graph()
    graph_config = RunnableConfig(
        max_concurrency=4,
        recursion_limit=50,
    )
    res = graph.invoke(
        input={"recognized": True},
        config=graph_config,
    )
    formatted_res = format_answer(res)
    play_audio(formatted_res.content)
    save_results(graph)


if __name__ == "__main__":
    main()
