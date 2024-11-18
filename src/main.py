# src/main.py

import os
import sys
from pathlib import Path

# 定义项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent

from utils.logger import LOG
from dotenv import load_dotenv
import gradio as gr

from backend.compiler.local_compiler_service import LocalCompilerService
from backend.exercise.exercise_service import ExerciseService
from frontend.tabs.compiler_tab import CompilerTab
from frontend.tabs.exercise_tab.exercise_tab import ExerciseTab
from frontend.components.welcome import get_welcome_markdown

# 加载环境变量
load_dotenv()

# 将 demo 设置为全局变量
css_path_compiler = str(ROOT_DIR / "src" / "frontend" / "static" / "css" / "compiler.css")
css_path_exercises = str(ROOT_DIR / "src" / "frontend" / "static" / "css" / "exercises.css")
# with open(css_path, "r", encoding="utf-8") as f:
#     css_content = f.read()



# 在模块级别直接创建界面
with gr.Blocks(title="EasyC - C语言在线编程平台", css_paths=[css_path_compiler, css_path_exercises]) as demo:
    gr.Markdown(get_welcome_markdown())

    compiler_service = LocalCompilerService()

    exercise_service = ExerciseService(compiler_service)
    ExerciseTab(exercise_service).create()

    CompilerTab(compiler_service).create()
    
def main():
    LOG.info("Starting EasyC application")
    LOG.info("Launching EasyC application")
    demo.launch(
        # server_name="0.0.0.0",
        # server_port=7860
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        LOG.exception(f"Application crashed: {e}")
        raise
