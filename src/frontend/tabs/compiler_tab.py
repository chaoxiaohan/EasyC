# frontend/tabs/compiler_tab.py

import gradio as gr
from backend.compiler.local_compiler_service import LocalCompilerService


def create_compiler_tab(compiler_service: LocalCompilerService):
    with gr.Tab("代码编译"):
        with gr.Row():
            # 状态提示组件（初始隐藏）
            success_message = gr.Markdown(
                value="",
                visible=False
            )

            with gr.Column() as settings_modal:
                
                settings_status = gr.Markdown(
                    value="请先配置 API 信息",
                    visible=True
                )
                # # # 状态提示组件
                # # settings_status = gr.Markdown(visible=False)

                # client_id_input = gr.Textbox(
                #     label="Client ID",
                #     placeholder="请输入 JDoodle Client ID",
                #     type="text",
                # )
                # client_secret_input = gr.Textbox(
                #     label="Client Secret",
                #     placeholder="请输入 JDoodle Client Secret",
                #     type="password",
                # )
                api_key_input = gr.Textbox(
                    label="API Key",
                    placeholder="请输入 DeepSeek API Key",
                    type="password",
                )
                save_settings_button = gr.Button("保存设置", variant="primary")

            # 添加设置保存函数
            def save_settings(api_key):
                compiler_service.update_credentials(api_key)
                return [
                    gr.update(visible=False),
                    gr.update(visible=True, value="✅ 配置已成功保存！您现在可以开始编程练习了。")
                ]
            
            save_settings_button.click(
                fn=save_settings,
                inputs=[api_key_input],
                outputs=[settings_modal, success_message]
            )
            

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
                    # save_button = gr.Button("保存代码")
                    
                # with gr.Row():
                #     file_upload = gr.File(label="上传代码文件")
                #     file_download = gr.Textbox(label="保存文件名", placeholder="example.c")
            
            # 右侧输出区域
            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="运行结果",
                    lines=5
                )
                
                # 新增 AI 反馈区域
                ai_feedback = gr.Markdown(
                    label="AI 反馈",
                    value="*等待代码运行完成后进行分析...*",
                    visible=True
                )
                
                # history_df = gr.DataFrame(
                #     label="代码历史记录",
                #     headers=["ID", "代码", "时间", "结果"],
                #     interactive=False
                # )
            
            async def run_code(code, input_data):
                result = await compiler_service.compile_and_run(code, input_data)
                return [result["output"], result, "*AI 分析中...*"]
            
            async def get_ai_feedback(code, output):
                analysis = await compiler_service.get_ai_feedback(code, output)
                return analysis
                     

            run_button.click(
                fn=run_code,
                inputs=[code_input, program_input],
                outputs=[output, gr.State(), ai_feedback]
            ).then(
                fn=get_ai_feedback,
                inputs=[code_input, gr.State()],
                outputs=[ai_feedback]
            )

        

        