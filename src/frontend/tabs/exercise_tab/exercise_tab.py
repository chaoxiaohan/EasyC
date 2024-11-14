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
        exercise_id = evt.value
        LOG.info(f"Selecting exercise: {exercise_id}")
        exercise = self.exercise_service.get_exercise_by_id(exercise_id)
        self.current_exercise = exercise_id
        
        return f"### {exercise.title}\n\n{exercise.description}"
    
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
    
    def create(self):
        """创建习题练习标签页"""
        with gr.Tab("习题练习"):
            with gr.Row():
                # 左侧：章节和习题列表
                with gr.Column(scale=1):
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
                    )
                
                # 右侧：习题详情和代码编辑器
                with gr.Column(scale=2):
                    exercise_description = gr.Markdown("请选择一个习题")
                    code_editor = gr.Code(
                        language="c",
                        label="编写代码",
                        elem_classes=["code-editor"],
                    )
                    run_btn = gr.Button("运行", variant="primary")
                    output_box = gr.Textbox(
                        label="运行结果",
                        lines=5,
                        placeholder="运行结果将显示在这里"
                    )
                    
            # 事件绑定
            chapter_dropdown.change(
                fn=self._handle_chapter_select,
                inputs=[chapter_dropdown],
                outputs=exercise_list
            )
            
            # Dataset 的 select 事件
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