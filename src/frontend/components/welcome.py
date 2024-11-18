# src/frontend/components/welcome.py

import gradio as gr


class Welcome:
    def __init__(self):
        self.markdown = gr.Markdown()

    def create(self):
        with gr.Row():
            with gr.Column():
                self.exercise_entry = gr.Button("📝 在线编程练习")
                self.exercise_introduction = gr.Markdown(
                    """- 精选编程习题，由易到难
- 实时评测系统，即时反馈
- AI 智能点评，指出改进方向"""
                )
            with gr.Column():
                self.compiler_entry = gr.Button("🔧 在线编译器")
                self.compiler_introduction = gr.Markdown(
                    """- 支持完整的 C 语言编程环境
- 实时编译运行，快速验证代码
- AI 代码分析，提供优化建议"""
                )

def get_welcome_markdown():
    return """
    # EasyC 🚀 - 实时 AI 评测，助你快速提升编程能力

    欢迎使用 EasyC，您的 C 语言编程学习助手！本平台提供两大核心功能：

    ### 📝 在线编程练习
    - 精选编程习题，由易到难
    - 实时评测系统，即时反馈
    - AI 智能点评，指出改进方向
    
    ### 🔧 在线编译器
    - 支持完整的 C 语言编程环境
    - 实时编译运行，快速验证代码
    - AI 代码分析，提供优化建议

    > 💡 提示：配置 API Key 后可启用 AI 分析功能，获得更专业的代码建议
    """