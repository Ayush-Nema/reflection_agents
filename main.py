"""
Graph implementation
=======================
Holds the LangGraph graph implementation
"""
from typing import List, Sequence

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

from chains import generation_chain, reflection_chain

load_dotenv()

# Node names
REFLECT = "reflect"
GENERATE = "generate"


def generation_node(state: Sequence[BaseMessage]):
    return generation_chain.invoke({"messages": state})


def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflection_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]  # fooling LLM to think that Human is messages to keep conversation alive


builder = MessageGraph()
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)


def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return REFLECT


builder.add_conditional_edges(GENERATE, should_continue)
builder.add_edge(REFLECT, GENERATE)

# Compile graph
graph = builder.compile()

# Visualize graph
# print(graph.get_graph().draw_mermaid())
# print(graph.get_graph().draw_ascii())

if __name__ == '__main__':
    inputs = HumanMessage(
        content="""Make this tweet better.
        @LangChainAI
        - newly tool calling feature is really underrated.
        
        After a long wait, finally it is here making the implementation of agents across different models with 
        function calling - super easy.
        
        Made a video covering their newest blog post.
        """
    )

    response = graph.invoke(inputs)
    print(response)
