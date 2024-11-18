# frontend/tabs/compiler_tab.py
import time
import pyperclip
import gradio as gr
from backend.compiler.local_compiler_service import LocalCompilerService


class CompilerTab:
    def __init__(self, compiler_service: LocalCompilerService):
        self.compiler_service = compiler_service

    def _show_settings(self):
        """显示设置面板"""
        return [
            gr.update(visible=True),  # 显示 API Key 输入框
            gr.update(visible=True),  # 显示保存按钮
            gr.update(visible=False, value="")
        ]
    
    def _save_settings(self, api_key: str):
        """保存设置"""
        self.compiler_service.update_credentials(api_key)
        return [
            gr.update(visible=False),  # 隐藏 API Key 输入框
            gr.update(visible=False),  # 隐藏保存按钮
            gr.update(visible=True, value="✅ 配置已成功保存！您现在可以开始编程练习了。")
        ]

    def _copy_feedback(self, markdown_text: str):
        return gr.update(visible=True)
    
    def _hide_status(self):
        time.sleep(3)
        return gr.update(visible=False)
    
    def _clean_feedback(self):
        return "*点击按钮开始分析*"
    
    async def _run_code(self, code: str, input_data: str):
        result = await self.compiler_service.compile_and_run(code, input_data)
        return [result["output"], result]
    
    def _get_ai_feedback_start(self):
        return "*AI 分析中...*"

    async def _get_ai_feedback(self, code: str, output):
        analysis = await self.compiler_service.get_ai_feedback(code, output)
        return analysis

    def _clean_code(self):
        return [
            gr.update(value=""),  # 清空代码输入
            gr.update(value=""),  # 清空程序输入
            gr.update(value=""),  # 清空运行结果
        ]
    
    def create(self):
        with gr.Tab("代码编译"):
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
                                label="程序输入（在这里输入程序运行时需要的输入值）",
                                placeholder="多个输入值请用空格分隔，例如: 1 2 3",
                                lines=2,
                                elem_classes=["program-input"]
                            )
                            
                            with gr.Row(elem_classes=["button-group"]):
                                run_button = gr.Button("▶ 运行", variant="primary", elem_classes=["action-button", "run-button"])
                                clean_button = gr.Button("🗑 清空", variant="secondary", elem_classes=["action-button", "clear-button"])
                
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
            
            save_settings_button.click(
                fn=self._save_settings,
                inputs=[api_key_input],
                outputs=[api_key_input, save_settings_button, success_message]
            )
            settings_button.click(
                fn=self._show_settings,
                outputs=[api_key_input, save_settings_button, success_message]
            )    
            
            run_button.click(
                fn=self._clean_feedback,
                outputs=[ai_feedback]
            ).then(
                fn=self._run_code,
                inputs=[code_input, program_input],
                outputs=[output, gr.State()]
            )

            get_ai_feedback_button.click(
                fn=self._get_ai_feedback_start,
                outputs=[ai_feedback]
            ).then(
                fn=self._get_ai_feedback,
                inputs=[code_input, gr.State()],
                outputs=[ai_feedback]
            )

            copy_button.click(
                fn=self._copy_feedback,
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
                fn=self._hide_status,
                outputs=[copy_status]
            )

                
            clean_button.click(
                fn=self._clean_code,
                outputs=[code_input, program_input, output]
            )
