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
from backend.ai.feedback_service import AIFeedbackService
from frontend.tabs.compiler_tab import CompilerTab
from frontend.tabs.exercise_tab import ExerciseTab
from frontend.tabs.welcome_tab import WelcomeTab
from frontend.tabs.settings_tab import SettingsTab

# 加载环境变量
load_dotenv()

# 将 demo 设置为全局变量
compiler_css_path = str(ROOT_DIR / "src" / "frontend" / "static" / "css" / "compiler.css")
exercises_css_path = str(ROOT_DIR / "src" / "frontend" / "static" / "css" / "exercises.css")
welcome_css_path = str(ROOT_DIR / "src" / "frontend" / "static" / "css" / "welcome.css")


with gr.Blocks(
    title="EasyC - C语言在线编程平台",
    css_paths=[compiler_css_path, exercises_css_path, welcome_css_path],
    # theme=gr.themes.Glass(),
) as demo:
    
        WelcomeTab().create()

        compiler_service = LocalCompilerService()
        feedback_service = AIFeedbackService()
        exercise_service = ExerciseService(compiler_service)

        ExerciseTab(exercise_service, compiler_service, feedback_service).create()
        CompilerTab(compiler_service, feedback_service).create()
        SettingsTab(feedback_service).create()


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
