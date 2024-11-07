# src/backend/ai/feedback_service.py

from utils.logger import logger
from .feedback_engine import AIFeedbackEngine

class AIFeedbackService:
    def __init__(self):
        self.engine = AIFeedbackEngine()
        logger.info(f"AIFeedbackService initialized")
    
    async def get_feedback(self, code: str, compile_result: dict) -> str:
        """根据代码和编译结果提供 AI 反馈"""
        logger.debug(f"Getting feedback for code: {code} and compile result: {compile_result}")

        message = f"""
## 代码分析
{code}

### 编译结果
{compile_result}

请分析以上代码和结果，给出：
1. 代码运行情况说明
2. 错误原因（如果有,没有可以不写）
3. 改进建议
"""
        try:
            feedback = self.engine.chat(message)
            logger.info("AI feedback generated successfully")
            return feedback
        except Exception as e:
            logger.error(f"Error generating AI feedback: {e}")
            return "AI 分析服务暂时不可用，请稍后再试。"
            