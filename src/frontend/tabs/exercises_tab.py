# src/tabs/exercises_tab.py

import gradio as gr
from EasyC.backend.compiler.jdoodle_compiler_service import CompilerService


def create_exercises_tab(compiler_service: CompilerService): 
    # Tab 1: 习题练习
    with gr.Tab("习题练习"):
        with gr.Row():
            with gr.Column(scale=1):
                # 习题描述区域
                exercise_description = gr.Markdown("""请输出 Hello, World!""")
                test_cases = gr.Dataframe(
                    headers=["输入", "预期输出"],
                    interactive=False
                )
            
            with gr.Column(scale=2):
                # 代码编辑区
                code_editor = gr.Code(
                    language="c",
                    label="代码编辑器"
                )
                # 输出结果区
                output_area = gr.Textbox(
                    label="运行结果",
                    lines=5
                )
                
                with gr.Row():
                    run_btn = gr.Button("运行")
                    debug_btn = gr.Button("调试")
                
                # 事件处理
                run_btn.click(fn=compiler_service.compile_and_run, inputs=[code_editor], outputs=[output_area])
                # debug_btn.click(fn=compiler_service.debug_code, inputs=[code_editor], outputs=[output_area])
