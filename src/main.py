# src/main.py

import os
import sys
# 添加项目根目录到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("main"))))

from utils.logger import logger
from dotenv import load_dotenv
import gradio as gr

from backend.compiler.compiler_service import CompilerService
from frontend.tabs.exercises_tab import create_exercises_tab
from frontend.tabs.compiler_tab import create_compiler_tab

# 加载环境变量
load_dotenv()

def main():
    logger.info("Starting EasyC application")

    # 初始化编译器服务
    compiler_service = CompilerService(
        client_id=os.getenv('JDOODLE_CLIENT_ID'),
        client_secret=os.getenv('JDOODLE_CLIENT_SECRET'),
        api_url="https://api.jdoodle.com/v1/execute"
    )
    
    # 创建 Gradio 界面
    with gr.Blocks(title="EasyC - C语言在线编程学习平台") as demo:
        with gr.Tabs():
            create_compiler_tab(compiler_service)
            create_exercises_tab(compiler_service)
    
    logger.info("Launching EasyC application")
    demo.launch()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"Application crashed: {e}")
        raise
