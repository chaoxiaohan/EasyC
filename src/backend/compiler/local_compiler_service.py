# backend/compiler/local_compiler_service.py

import os
import subprocess
import uuid
from typing import Dict, Optional
from utils.logger import logger
from backend.ai.feedback_service import AIFeedbackService

class LocalCompilerService:
    def __init__(self, api_key: str = None):
        self.compile_dir = "/tmp/compile"
        self.feedback_service = None
        
        # 创建编译目录
        os.makedirs(self.compile_dir, exist_ok=True)
        logger.info(f"LocalCompilerService initialized with compile_dir: {self.compile_dir}")

    async def compile_and_run(self, code: str, input_data: Optional[str] = None) -> Dict:
        """编译并运行代码"""
        source_file = None
        output_file = None
        try:
            logger.info(f"Compiling and running code: {code}")
            
            # 确保编译目录存在
            os.makedirs(self.compile_dir, exist_ok=True)
            
            # 生成唯一的文件名
            file_id = str(uuid.uuid4())
            source_file = os.path.join(self.compile_dir, f"{file_id}.c")
            
            # 保存源代码
            with open(source_file, "w") as f:
                f.write(code)
            
            # 编译代码
            output_file = os.path.join(self.compile_dir, file_id)
            compile_result = subprocess.run(
                ["gcc", source_file, "-o", output_file],
                capture_output=True,
                text=True
            )
            
            if compile_result.returncode != 0:
                output = f"❌ 编译错误:\n{compile_result.stderr}"
                return {
                    "success": False,
                    "output": output,
                    "error": compile_result.stderr,
                    "execution_time": 0.0
                }
            
            # 运行程序
            try:
                run_result = subprocess.run(
                    [output_file],
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=5  # 添加超时限制
                )
                
                if run_result.returncode == 0:
                    output = f"✅ 运行成功！程序输出:\n{run_result.stdout}"
                else:
                    output = f"❌ 运行错误:\n{run_result.stderr}"
                
                return {
                    "success": run_result.returncode == 0,
                    "output": output,
                    "error": run_result.stderr,
                    "execution_time": 0.0  # 本地运行暂不计算执行时间
                }
                
            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "output": "❌ 程序执行超时",
                    "error": "Execution timeout",
                    "execution_time": 5.0
                }
                
        except Exception as e:
            logger.exception("Error in compile_and_run")
            return {
                "success": False,
                "output": f"❌ 运行错误: {str(e)}",
                "error": str(e),
                "execution_time": 0.0
            }
            
        finally:
            # 清理临时文件
            if os.path.exists(source_file):
                os.remove(source_file)
            if os.path.exists(output_file):
                os.remove(output_file)

    def update_credentials(self, api_key: str) -> bool:
        """更新凭证，主要是用于设置 API Key"""
        try:
            # 重新初始化 feedback service
            self.feedback_service = AIFeedbackService(api_key=api_key)
            logger.info("Credentials updated successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to update credentials: {e}")
            return False


    async def get_ai_feedback(self, code: str, output: dict) -> str:
        """获取 AI 反馈"""
        if not self.feedback_service:
            return "请先在设置中配置 API Key 以启用 AI 反馈功能"
        try:
            return await self.feedback_service.get_feedback(code, output)
        except Exception as e:
            logger.error(f"Error getting AI feedback: {e}")
            return f"获取 AI 反馈时出错: {str(e)}"