"""
Chains
=============
File to hold our prompts and chains for use our LangGraph
"""
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

# This prompt acts like a critic
reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral Twitter influence grading a tweet. Generate critique and recommendations for the user's "
            "tweet. Always provide detailed recommendations, including requests for length, virality, style etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a Twitter Techie influencer assistant tasked with writing excellent Twitter posts. "
            " Generate best Twitter post possible for the user's request."
            " If the user provides critique, respond with the revised version of the previous attempts."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatOpenAI()
generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm
