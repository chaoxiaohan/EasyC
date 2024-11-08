# src/main.py

import os
import sys

# 切换到脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
print(project_dir)
os.chdir(project_dir)

from utils.logger import logger
from dotenv import load_dotenv
import gradio as gr

from backend.compiler.local_compiler_service import LocalCompilerService
from frontend.tabs.compiler_tab import create_compiler_tab

# 加载环境变量
load_dotenv()

def main():
    logger.info("Starting EasyC application")

    compiler_service = LocalCompilerService()
    
    # 创建 Gradio 界面
    with gr.Blocks(title="EasyC - C语言在线编程学习平台") as demo:
        gr.Markdown("""
    # EasyC - C语言在线编程平台
    
    ### 功能说明：
    1. 支持C语言编程
    2. 如果程序需要输入，请在输入框中提供
    3. 点击运行查看结果
    4. AI 会对结果进行分析，并给出改进建议
    """)
        with gr.Tabs():
            create_compiler_tab(compiler_service)
            # create_exercises_tab(compiler_service)
    
    logger.info("Launching EasyC application")
    demo.launch(
        # server_name="0.0.0.0",
        # server_port=7860
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Application crashed: {e}")
        raise