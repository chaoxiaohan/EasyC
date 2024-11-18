# src/frontend/tabs/exercise_tab/exercise_tab.py

from utils.logger import LOG
import gradio as gr
from typing import Optional
from backend.exercise.exercise_service import ExerciseService



class ExerciseTab:
    def __init__(self, exercise_service: ExerciseService):
        self.exercise_service = exercise_service
        self.current_exercise: Optional[str] = None

    def _handle_chapter_select(self, chapter_id: str):
        """处理章节选择"""
        LOG.info(f"Selecting chapter: {chapter_id}")
        exercises = self.exercise_service.get_exercises_by_chapter(chapter_id)
        return [[exercise.id, exercise.title, exercise.difficulty] for exercise in exercises]

    def _handle_exercise_select(self, evt: gr.SelectData):
        """处理习题选择"""
        if evt.index[1] != 0:
            return gr.update()
        exercise_id = evt.value
        self.current_exercise = exercise_id
        LOG.info(f"Selecting exercise: {exercise_id}")
        exercise = self.exercise_service.get_exercise_by_id(exercise_id)
        test_description = f"### 题目：{exercise.title}\n\n{exercise.description}"
        for i, test_case in enumerate(exercise.test_cases, 1):
            test_description += f"\n##### case {i}: \n&nbsp;&nbsp;&nbsp;&nbsp;**输入**: {test_case.input}  \n&nbsp;&nbsp;&nbsp;&nbsp;**输出**: {test_case.expected_output}"
        return test_description
    
    async def _handle_run_code(self, code: str):
        """处理代码运行"""
        if not self.current_exercise:
            LOG.warning("Attempted to run code without selecting an exercise")
            return "请先选择一个习题"
        
        LOG.info(f"Running code for exercise: {self.current_exercise}")
        try:
            result = await self.exercise_service.run_code(self.current_exercise, code)
            return result["output"]
        except Exception as e:
            LOG.error(f"Error running code: {e}")
            return f"运行代码时出错: {e}"
    
    def _clean_code(self):
        return [
            gr.update(value=""),
            gr.update(value=""),
            gr.update(value=""),
        ]
    
    def create(self):
        """创建习题练习标签页"""
        with gr.Tab("习题练习"):
            with gr.Column():
                # 左侧：章节和习题列表
                with gr.Row():
                    with gr.Column():
                        chapter_dropdown = gr.Dropdown(
                            choices=[c["id"] for c in self.exercise_service.get_chapters()],
                            interactive=True,
                            value="chapter1",
                            label="选择章节",
                        )
                        
                        exercise_list = gr.Dataframe(
                            value=[[ex.id, ex.title, ex.difficulty] for ex in self.exercise_service.get_exercises_by_chapter("chapter1")],
                            headers=["id","题目", "难度"],
                            interactive=False,
                            label="习题列表",
                            elem_classes=["exercise-list"]
                        )
                    exercise_description = gr.Markdown("请选择一个习题")
                
                # 右侧：习题详情和代码编辑器
                with gr.Row():
                    with gr.Column():
                        # 左侧代码编辑区
                        with gr.Column():
                            code_editor = gr.Code(
                                language="c",
                                label="编写代码",
                                lines=15,  # 增加代码编辑器高度
                                elem_classes=["code-editor"],
                            )
                            program_input = gr.Textbox(
                                label="程序输入（在这里输入程序运行时需要的所有输入值）",
                                placeholder="""多个输入值请用空格分隔，例如: 1 2 3""",
                                lines=3,
                                elem_classes=["program-input"]
                            )
                            with gr.Row():
                                run_btn = gr.Button("▶ 运行", variant="primary")
                                clean_btn = gr.Button("🗑 清空")
                    with gr.Column():    
                        output_box = gr.Textbox(
                            label="运行结果",
                            lines=8,
                            placeholder="运行结果将显示在这里"
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
                    
            # 事件绑定
            chapter_dropdown.change(
                fn=self._handle_chapter_select,
                inputs=[chapter_dropdown],
                outputs=exercise_list
            )
            
            exercise_list.select(
                fn=self._handle_exercise_select,
                outputs=[exercise_description]
            )
            
            run_btn.click(
                fn=self._handle_run_code,
                inputs=[code_editor],
                outputs=[output_box],
                api_name="run_code"  # 添加API名称
            )

            clean_btn.click(
                fn=self._clean_code,
                outputs=[code_editor, program_input, output_box]
            )
