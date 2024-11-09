# frontend/tabs/compiler_tab.py
import time
import pyperclip
import gradio as gr
from backend.compiler.local_compiler_service import LocalCompilerService


def create_compiler_tab(compiler_service: LocalCompilerService):
    with gr.Tab("代码编译"):
        # 顶部工具栏和设置区域
        with gr.Column():
            # 设置面板
            settings_button = gr.Button(
                value="⚙️ 配置 API 信息",
                visible=True,
                size="sm",
                scale=1
            )

            api_key_input = gr.Textbox(
                label="API Key",
                placeholder="请输入 DeepSeek API Key",
                type="password",
            )

            save_settings_button = gr.Button("保存设置", variant="primary", size="sm", scale=1)

            # 状态提示组件（初始隐藏）
            success_message = gr.Markdown(
                value="",
                visible=False
            )

            # 添加设置显示函数
            def show_settings():
                return [
                    gr.update(visible=True),  # 显示 API Key 输入框
                    gr.update(visible=True),  # 显示保存按钮
                    gr.update(visible=False, value="")
                ]
            # 添加设置保存函数
            def save_settings(api_key):
                compiler_service.update_credentials(api_key)
                return [
                    gr.update(visible=False),  # 隐藏 API Key 输入框
                    gr.update(visible=False),  # 隐藏保存按钮
                    gr.update(visible=True, value="✅ 配置已成功保存！您现在可以开始编程练习了。")  # 显示成功提示
                ]
            
            save_settings_button.click(
                fn=save_settings,
                inputs=[api_key_input],
                outputs=[api_key_input, save_settings_button, success_message]
            )
            settings_button.click(
                fn=show_settings,
                outputs=[api_key_input, save_settings_button, success_message]
            )
        # 代码编辑区域
        with gr.Row():
            # 左侧编辑区域
            with gr.Column(scale=2):
                code_input = gr.Code(
                    label="C 代码编辑器",
                    language="c",
                    lines=10,
                    show_label=True,
                    wrap_lines=True,
                    container=True,
                )
                
                program_input = gr.Textbox(
                    label="程序输入（如果需要）",
                    placeholder="多个输入值请用空格分隔, 例如: 1 2 3",
                    lines=2
                )
                
                with gr.Row():
                    run_button = gr.Button("运行代码", variant="primary")
                    clear_button = gr.Button("清空代码", variant="secondary")
                    # save_button = gr.Button("保存代码")
                
                # with gr.Row():
                #     file_upload = gr.File(label="上传代码文件")
                #     file_download = gr.Textbox(label="保存文件名", placeholder="example.c")
            
            # 右侧输出区域
            with gr.Column(scale=1):
                output = gr.Textbox(
                    label="运行结果",
                    lines=5,
                    show_copy_button=True
                )
                
                # 新增 AI 反馈区域
                ai_feedback = gr.Markdown(
                    label="AI 反馈",
                    value="*等待代码运行完成后进行分析...*",
                    visible=True,
                    elem_classes=["feedback-text"]
                )
                with gr.Row():
                    copy_button = gr.Button("📋 复制反馈", size="sm")
                    copy_status = gr.Markdown(value="✅ 已复制到剪贴板！", visible=False)  # 添加状态提示组件

                # history_df = gr.DataFrame(
                #     label="代码历史记录",
                #     headers=["ID", "代码", "时间", "结果"],
                #     interactive=False
                # )

                def copy_feedback(markdown_text):
                    return gr.update(visible=True)
                
                def hide_status():
                    time.sleep(3)
                    return gr.update(visible=False)
                
                async def run_code(code, input_data):
                    result = await compiler_service.compile_and_run(code, input_data)
                    return [result["output"], result, "*AI 分析中...*", gr.update(visible=True)]
                
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

                copy_button.click(
                    fn=copy_feedback,
                    inputs=[ai_feedback],
                    outputs=[copy_status],
                    js="""
                    async (markdown) => {
                        // 获取 Markdown 内容，移除 Markdown 语法
                        let text = markdown.replace(/\*/g, '').trim();
                        
                        try {
                            await navigator.clipboard.writeText(text);
                            return true;
                        } catch (err) {
                            // 降级方案：为了兼容性，使用传统的方法
                            const textarea = document.createElement('textarea');
                            textarea.value = text;
                            document.body.appendChild(textarea);
                            textarea.select();
                            try {
                                document.execCommand('copy');
                                document.body.removeChild(textarea);
                                return true;
                            } catch (err) {
                                document.body.removeChild(textarea);
                                console.error('Failed to copy text: ', err);
                                return false;
                            }
                        }
                    }
                    """
                ).success(
                fn=hide_status,
                outputs=[copy_status]
            )

            def clean_code():
                    return [
                        gr.update(value=""),  # 清空代码输入
                        gr.update(value=""),  # 清空程序输入
                        gr.update(value=""),  # 清空运行结果
                        gr.update(value="*等待代码运行完成后进行分析...*")  # 清空 AI 反馈
                    ]
                
            clear_button.click(
                fn=clean_code,
                outputs=[code_input, program_input, output, ai_feedback]
            )
    