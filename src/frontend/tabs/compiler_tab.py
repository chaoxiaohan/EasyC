# frontend/tabs/compiler_tab.py
import time
import pyperclip
import gradio as gr
from backend.compiler.local_compiler_service import LocalCompilerService



def create_compiler_tab(compiler_service: LocalCompilerService):
    with gr.Tab("代码编译"):
        # 添加 CSS 类名到相应组件
        # 顶部工具栏和设置区域
        with gr.Column():
            # 设置面板
            settings_button = gr.Button(
                value="⚙️ 配置 API_KEY",
                visible=True,
                size="md",
                elem_classes=["settings-button"]
            )

            api_key_input = gr.Textbox(
                label="API Key",
                placeholder="请输入 DeepSeek API Key",
                type="password",
                elem_classes=["api-key-input"]
            )

            save_settings_button = gr.Button(
                "保存设置",
                variant="primary",
                size="sm",
                elem_classes=["save-settings-button"]
            )

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
            with gr.Column(scale=3, elem_classes=["editor-column"]):
                with gr.Column(elem_classes=["editor-card"]):
                    code_input = gr.Code(
                        label="C 代码编辑器",
                        language="c",
                        lines=15,  # 增加默认行数
                        show_label=True,
                        wrap_lines=True,
                        container=True,
                        elem_classes=["code-editor"]
                    )
                    
                    with gr.Column(elem_classes=["input-control-group"]):
                        program_input = gr.Textbox(
                            label="程序输入",
                            placeholder="多个输入值请用空格分隔, 例如: 1 2 3",
                            lines=2,
                            elem_classes=["program-input"]
                        )
                        
                        with gr.Row(elem_classes=["button-group"]):
                            run_button = gr.Button("▶ 运行", variant="primary", elem_classes=["action-button", "run-button"])
                            clear_button = gr.Button("🗑 清空", variant="secondary", elem_classes=["action-button", "clear-button"])
            
            # 右侧输出区域
            with gr.Column(scale=2, elem_classes=["output-column"]):
                with gr.Column(elem_classes=["output-card"]):
                    output = gr.Textbox(
                        label="运行结果",
                        lines=6,
                        show_copy_button=True,
                        elem_classes=["output-area"]
                    )

                    get_ai_feedback_button = gr.Button(
                        "🤖 AI 分析",  # 添加图标并修改文本
                        value=False,
                        interactive=True,
                        variant="primary",
                        # size="sm",
                        elem_classes=["get-ai-feedback-button"]
                    )
                    
                    ai_feedback = gr.Markdown(
                        value="*点击按钮开始分析*",
                        elem_classes=["feedback-area"]
                    )

                    copy_button = gr.Button(
                        "📋 复制分析结果",  # 修改按钮文本,
                        size="sm",
                        elem_classes=["copy-button"]
                    )
                    
                    copy_status = gr.Markdown(
                        value="✅ 已复制到剪贴板！", 
                        visible=False,
                        elem_classes=["copy-status"]
                    )

                def copy_feedback(markdown_text):
                    return gr.update(visible=True)
                
                def hide_status():
                    time.sleep(3)
                    return gr.update(visible=False)
                
                def clean_feedback():
                    return "*点击按钮开始分析*"
                
                async def run_code(code, input_data):
                    result = await compiler_service.compile_and_run(code, input_data)
                    return [result["output"], result]
                
                def get_ai_feedback_start():
                    return "*AI 分析中...*"

                async def get_ai_feedback(code, output):
                    analysis = await compiler_service.get_ai_feedback(code, output)
                    return analysis
                
                
                run_button.click(
                    fn=clean_feedback,
                    outputs=[ai_feedback]
                ).then(
                    fn=run_code,
                    inputs=[code_input, program_input],
                    outputs=[output, gr.State()]
                )

                get_ai_feedback_button.click(
                    fn=get_ai_feedback_start,
                    outputs=[ai_feedback]
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
                        gr.update(value="*点击按钮开始分析*")  # 清空 AI 反馈
                    ]
                
            clear_button.click(
                fn=clean_code,
                outputs=[code_input, program_input, output, ai_feedback]
            )
    