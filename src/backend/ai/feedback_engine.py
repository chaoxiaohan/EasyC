# src/backend/ai/feedback_engine.py

import os
from utils.logger import logger

from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]

class AIFeedbackEngine:
    def __init__(self, model: str="deepseek-chat", session_id: str=None):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        self.model = ChatOpenAI(model="deepseek-chat", openai_api_key=api_key, openai_api_base='https://api.deepseek.com',)
        self.session_id = session_id
        self.workflow = StateGraph(State)
        self.workflow.add_node("chat_model", self._chat_model)
        self.workflow.add_edge(START, "chat_model")
        self.workflow.add_edge("chat_model", END)
        self.memory_saver = MemorySaver()
        if self.session_id:
            self.graph = self.workflow.compile(self.memory_saver)
        else:
            self.graph = self.workflow.compile()
        logger.info(f"AIFeedbackEngine initialized with model: {model}, session_id: {session_id}")
    def _chat_model(self, messages):
        res = self.model.invoke(messages['messages'])
        return {"messages": [res]}
    
    def chat(self, message):
        logger.debug(f"Chatting with message: {message}")
        messages = [HumanMessage(content=message)]
        try:
            res = self.graph.invoke({"messages": messages})
            logger.debug(f"Chat response generated successfully")
            return res["messages"][-1].content
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            raise
    
    def chat_with_history(self, message):
        logger.debug(f"Chatting with message: {message}")
        config = {"configurable": {"thread_id": self.session_id}}
        messages = [HumanMessage(content=message)]
        try:
            res = self.graph.invoke({"messages": messages}, config=config)
            logger.debug(f"Chat response generated successfully")
            return res["messages"][-1].content
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            raise
    
    