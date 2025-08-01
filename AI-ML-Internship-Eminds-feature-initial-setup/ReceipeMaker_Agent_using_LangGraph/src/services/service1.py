from src.services.graph import get_graph

def get_dinner_idea(user_input: str) -> str:
    graph = get_graph()
    result = graph.invoke({"input": user_input})
    # LangGraph returns a dict with the final state
    return result.get("suggestion", "No suggestion was generated.")
