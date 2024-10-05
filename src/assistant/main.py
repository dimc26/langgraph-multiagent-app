from langgraph.graph.state import CompiledGraph, RunnableConfig

from assistant.graph.decider_graph import build_assistant_graph
from assistant.utils.text_to_speech import play_answer


def save_results(graph: CompiledGraph) -> None:
    with open("graph.png", "wb") as f:
        f.write(graph.get_graph(xray=1).draw_mermaid_png())


def main() -> None:
    graph = build_assistant_graph()
    graph_config = RunnableConfig(
        max_concurrency=2,
        recursion_limit=50,
    )
    res = graph.invoke(
        input={"recognized": True},
        config=graph_config,
    )
    print(res)
    save_results(graph)
    play_answer("Ya he gestionado tu petición")

if __name__ == "__main__":
    main()
