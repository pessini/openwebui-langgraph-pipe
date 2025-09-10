from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.types import interrupt
from langchain_core.messages import AIMessage


class AgentState(MessagesState):
    user_input: str = ""


def menu_node(state: AgentState) -> AgentState:
    """Shows menu and interrupts for user input."""
    value = interrupt("Choose a number:\nEnter eg. 1 or 2")
    state["user_input"] = value
    return state


def result_node(state: AgentState) -> AgentState:
    """Shows the result based on user choice."""
    choice = state.get("user_input", "")
     # Ensure messages is a list and append an AIMessage
    if "messages" not in state or not isinstance(state["messages"], list):
        state["messages"] = []
    state["messages"].append(AIMessage(content=f"You chose number: {choice}"))
    return state


# Build the graph
builder = StateGraph(AgentState)
builder.add_node("menu", menu_node)
builder.add_node("result", result_node)
builder.add_edge(START, "menu")
builder.add_edge("menu", "result")
builder.add_edge("result", END)

graph = builder.compile()
