# src/backend/ai/feedback_service.py

import json
from utils.logger import LOG
from .feedback_engine import AIFeedbackEngine

class AIFeedbackService:
    def __init__(self):
        self.engine = None
        LOG.info(f"AIFeedbackService initialized")

    # def update_api_key(self, api_key: str):
    #     self.engine = AIFeedbackEngine(api_key=api_key)

    def update_credentials(self, api_key: str) -> bool:
        """更新凭证，主要是用于设置 API Key"""
        if not api_key:
            self.engine = None
            return True
        
        try:
            self.engine = AIFeedbackEngine(api_key=api_key)
            LOG.info("Credentials updated successfully")
            return True
        except Exception as e:
            LOG.error(f"Failed to update credentials: {e}")
            return False
    
    async def get_feedback(self, code: str, compile_result: dict, input_data: str=None, exercise_description: str=None) -> str:
        """根据代码和编译结果提供 AI 反馈"""
        if not self.engine:
            return "请先在设置中配置 API Key 以启用 AI 反馈功能"
        
        LOG.debug(f"Getting feedback for code: {code} and compile result: {compile_result}")
        message = {
            "exercise_description": exercise_description,
            "code": code,
            "input_data": input_data,
            "compile_result": compile_result,
        }
        try:
            feedback = self.engine.chat(json.dumps(message))
            LOG.info("AI feedback generated successfully")
            return feedback
        except Exception as e:
            LOG.error(f"Error generating AI feedback: {e}")
            return "AI 分析服务暂时不可用，请稍后再试。"
            