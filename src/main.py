# src/main.py

import os
import sys
from pathlib import Path

# 定义项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent

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
    with gr.Blocks(title="EasyC - C语言在线编程平台") as demo:
        gr.Markdown("""
    # EasyC 🚀 - 实时 AI 评测，助你快速提升编程能力
    
    ### 功能说明：
    1. 支持C语言编程
    2. 如果程序需要输入，请在输入框中提供
    3. 点击运行查看结果
    4. 配置 api_key 后，AI 会自动对结果进行分析，并给出改进建议
    """)
        with gr.Tabs():
            create_compiler_tab(compiler_service)
    
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