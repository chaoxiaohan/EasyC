# frontend/tabs/compiler_tab.py
import time
import pyperclip
import gradio as gr
from backend.compiler.local_compiler_service import LocalCompilerService
from backend.ai.feedback_service import AIFeedbackService


class CompilerTab:
    def __init__(self, compiler_service: LocalCompilerService, feedback_service: AIFeedbackService):
        self.compiler_service = compiler_service
        self.feedback_service = feedback_service

    # def _copy_feedback(self, markdown_text: str):
    #     return gr.update(visible=True)
    
    def _hide_status(self):
        time.sleep(3)
        return gr.update(visible=False)
    
    def _clean_feedback(self):
        return "*点击按钮开始分析*"
    
    async def _run_code(self, code: str, input_data: str):
        result = await self.compiler_service.compile_and_run(code, input_data)
        return result["output"]
    def _get_ai_feedback_start(self):
        return "*AI 分析中...*"

    async def _get_ai_feedback(self, code: str, output: str, input_data: str):
        async for chunk in self.feedback_service.get_feedback(code=code, compile_result=output, input_data=input_data):
            yield chunk

    def _clean_code(self):
        return [
            gr.update(value=""),  # 清空代码输入
            gr.update(value=""),  # 清空程序输入
            gr.update(value=""),  # 清空运行结果
        ]
    
    def create(self):
        with gr.Tab("在线编译⚡"):
            with gr.Column():
                with gr.Row(elem_classes="split-columns"):
                    # 左侧编辑区域
                    with gr.Column(scale=3):
                        with gr.Column():
                            code_input = gr.Code(
                                label="C 代码编辑器",
                                language="c",
                                lines=24,
                                max_lines=24,
                                show_label=True,
                                wrap_lines=True,
                                container=True,
                                elem_classes=["code-editor"]
                            )
                            
                            with gr.Column():
                                program_input = gr.Textbox(
                                    label="程序输入（在这里一次性输入程序运行时需要的所有输入值）",
                                    placeholder="多个输入值请用空格分隔，例如: 1 2 3",
                                    max_lines=2,
                                )
                                
                                with gr.Row(elem_classes=["button-group"]):
                                    run_button = gr.Button("▶ 运行", variant="primary")
                                    clean_button = gr.Button("🗑 清空", variant="secondary")
                    
                    # 右侧输出区域
                    with gr.Column(scale=2, elem_classes=["output-card", "scrollable"]):
                        output = gr.Textbox(
                            label="运行结果",
                            lines=6,
                            placeholder="运行结果将显示在这里",
                            interactive=False,
                        )

                        with gr.Row(elem_classes=["button-group"]):
                            get_ai_feedback_button = gr.Button(
                                "🤖 AI 分析",  # 添加图标并修改文本
                                value=False,
                                interactive=True,
                                variant="primary",
                            )
                        
                        ai_feedback = gr.Markdown(
                            value="*点击按钮开始分析*",
                            show_copy_button=True,
                            elem_classes=["feedback-area"]
                        )

                            
            
            run_button.click(
                fn=self._clean_feedback,
                outputs=[ai_feedback]
            ).then(
                fn=self._run_code,
                inputs=[code_input, program_input],
                outputs=[output]
            )

            get_ai_feedback_button.click(
                fn=self._get_ai_feedback_start,
                outputs=[ai_feedback]
            ).then(
                fn=self._get_ai_feedback,
                inputs=[code_input, output, program_input],
                outputs=[ai_feedback]
            )

            # copy_button.click(
            #     fn=self._copy_feedback,
            #     inputs=[ai_feedback],
            #     outputs=[copy_status],
            #     js="""
            #     async (markdown) => {
            #         // 获取 Markdown 内容，移除 Markdown 语法
            #         let text = markdown.replace(/\*/g, '').trim();
                    
            #         try {
            #             await navigator.clipboard.writeText(text);
            #             return true;
            #         } catch (err) {
            #             // 降级方案：为了兼容性，使用传统的方法
            #             const textarea = document.createElement('textarea');
            #             textarea.value = text;
            #             document.body.appendChild(textarea);
            #             textarea.select();
            #             try {
            #                 document.execCommand('copy');
            #                 document.body.removeChild(textarea);
            #                 return true;
            #             } catch (err) {
            #                 document.body.removeChild(textarea);
            #                 console.error('Failed to copy text: ', err);
            #                 return false;
            #             }
            #         }
            #     }
            #     """
            # ).success(
            #     fn=self._hide_status,
            #     outputs=[copy_status]
            # )

                
            clean_button.click(
                fn=self._clean_code,
                outputs=[code_input, program_input, output]
            )
