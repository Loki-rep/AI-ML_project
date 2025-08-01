from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define the state schema
class GraphState(TypedDict):
    input: str
    suggestion: str

def run_llm(state: GraphState) -> GraphState:
    user_text = state["input"]
    template = (
        "You are a cooking assistant. Based on the input, suggest a dinner recipe idea.\n\n"
        "Input: {input}\n\nRecipe Idea:"
    )
    prompt = PromptTemplate(input_variables=["input"], template=template)

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192",
        temperature=0.7
    )

    chain = prompt | llm
    response = chain.invoke({"input": user_text})

    # ✅ Ensure we extract just the content
    return {"input": state["input"], "suggestion": response.content}
def get_graph() -> StateGraph:
    builder = StateGraph(GraphState)
    builder.add_node("suggest_recipe", RunnableLambda(run_llm))
    builder.set_entry_point("suggest_recipe")
    builder.add_edge("suggest_recipe", END)
    return builder.compile()
