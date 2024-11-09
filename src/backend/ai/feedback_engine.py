# src/backend/ai/feedback_engine.py

import os
import json
from utils.logger import logger
from utils.path_utils import ProjectPaths
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class AIFeedbackEngine:
    def __init__(self, model: str="deepseek-chat", api_key: str=None):
        prompt_path = ProjectPaths.get_project_path("prompts", "result_feedback_prompt.txt")
        with open(prompt_path, "r") as f:
            result_feedback_prompt = f.read().strip()
        self.system_message = ChatPromptTemplate(
            [
                ("system", result_feedback_prompt),
                ("user", "{messages}")
            ]
        )
        # api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_key = api_key
        self.model = self.system_message | ChatOpenAI(model="deepseek-chat", openai_api_key=self.api_key, openai_api_base='https://api.deepseek.com',)

    def update_api_key(self, api_key: str):
        self.api_key = api_key
        self.model = self.system_message | ChatOpenAI(model="deepseek-chat", openai_api_key=self.api_key, openai_api_base='https://api.deepseek.com',)
    
    def chat(self, message):
        logger.debug(f"Chatting with message: {message}")
        try:
            response = self.model.invoke({"messages": message})
            return response.content
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            raise

    
    