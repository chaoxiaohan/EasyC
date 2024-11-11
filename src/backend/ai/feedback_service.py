# src/backend/ai/feedback_service.py

import json
from utils.logger import logger
from .feedback_engine import AIFeedbackEngine

class AIFeedbackService:
    def __init__(self, api_key: str=None):
        self.api_key = api_key
        self.engine = AIFeedbackEngine(api_key=self.api_key)
        logger.info(f"AIFeedbackService initialized")

    def update_api_key(self, api_key: str):
        self.api_key = api_key
        self.engine.update_api_key(self.api_key)
    
    async def get_feedback(self, code: str, compile_result: dict) -> str:
        """根据代码和编译结果提供 AI 反馈"""
        logger.debug(f"Getting feedback for code: {code} and compile result: {compile_result}")
        message = {
            "code": code,
            "compile_result": compile_result
        }
        try:
            feedback = self.engine.chat(json.dumps(message))
            logger.info("AI feedback generated successfully")
            return feedback
        except Exception as e:
            logger.error(f"Error generating AI feedback: {e}")
            return "AI 分析服务暂时不可用，请稍后再试。"
            