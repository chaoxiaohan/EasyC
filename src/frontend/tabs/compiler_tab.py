# src/frontend/tabs/compiler_tab.py

import gradio as gr
from backend.compiler.compiler_service import CompilerService



def create_compiler_tab(compiler_service: CompilerService):
    with gr.Tab("代码编译"):
        with gr.Row():
            # 左侧编辑区域
            with gr.Column(scale=2):
                code_input = gr.Code(
                    label="C 代码编辑器",
                    language="c"
                )
                
                program_input = gr.Textbox(
                    label="程序输入（如果需要）",
                    placeholder="多个输入值请用空格分隔",
                    lines=2
                )
                
                with gr.Row():
                    run_button = gr.Button("运行代码", variant="primary")
                    save_button = gr.Button("保存代码")
                    
                with gr.Row():
                    file_upload = gr.File(label="上传代码文件")
                    file_download = gr.Textbox(label="保存文件名", placeholder="example.c")
            
            # 右侧输出区域
            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="运行结果",
                    lines=5
                )
                
                # 新增 AI 反馈区域
                ai_feedback = gr.Markdown(
                    label="AI 反馈",
                    value="等待代码运行...",
                    visible=True
                )
                
                history_df = gr.DataFrame(
                    label="代码历史记录",
                    headers=["ID", "代码", "时间", "结果"],
                    interactive=False
                )
            
            async def run_code(code, input_data):
                result = await compiler_service.compile_and_run(code, input_data)
                return (
                    result["output"],
                    result["ai_feedback"]
                )
            
            run_button.click(fn=run_code, inputs=[code_input, program_input], outputs=[output, ai_feedback])