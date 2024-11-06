# src/backend/compiler/compiler_service.py

from utils.logger import logger
import requests
from typing import Dict, Optional
from backend.ai.feedback_service import AIFeedbackService

class CompilerService:
    def __init__(self, client_id: str, client_secret: str, api_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_url = api_url
        self.feedback_service = AIFeedbackService()
        logger.info(f"CompilerService initialized with client_id: {client_id}, client_secret: {client_secret}, api_url: {api_url}")
    
    async def compile_and_run(self, code: str, input_data: Optional[str] = None) -> Dict:
        try:
            logger.info(f"Compiling and running code: {code}")

            # 构建请求体
            payload = {
                "clientId": self.client_id,
                "clientSecret": self.client_secret,
                "script": code,
                "language": "c",
                "versionIndex": "0",
                "stdin": input_data or ""
            }
            
            # 发送请求
            response = requests.post(self.api_url, json=payload)
            compile_result = response.json()
            logger.debug(f"Compilation result: {compile_result}")

            # 获取 AI 反馈
            ai_feedback = await self.feedback_service.get_feedback(code, compile_result)
            
            # 返回完整结果
            return {
                "success": not bool(compile_result.get("error")),
                "output": compile_result.get("output", ""),
                "error": compile_result.get("error", ""),
                "execution_time": float(compile_result.get("cpuTime")) if compile_result.get("cpuTime") is not None else 0.0,
                "ai_feedback": ai_feedback
            }

        except Exception as e:
            logger.exception("Error in compile_and_run")
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "execution_time": 0,
                "ai_feedback": "服务器出现错误，请稍后重试。"
            }
            