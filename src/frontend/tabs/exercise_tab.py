# src/frontend/tabs/exercise_tab/exercise_tab.py

from utils.logger import LOG
import gradio as gr
from typing import Optional
from backend.compiler.local_compiler_service import LocalCompilerService
from backend.exercise.exercise_service import ExerciseService
from backend.exercise.models.exercise import Exercise
from backend.ai.feedback_service import AIFeedbackService

class ExerciseTab:
    def __init__(self, exercise_service: ExerciseService, compiler_service: LocalCompilerService, feedback_service: AIFeedbackService):
        self.exercise_service = exercise_service
        self.compiler_service = compiler_service
        self.feedback_service = feedback_service
        self.current_exercise: Optional[Exercise] = None

    def _handle_chapter_select(self, chapter_id: str):
        """处理章节选择"""
        LOG.info(f"Selecting chapter: {chapter_id}")
        exercises = self.exercise_service.get_exercises_by_chapter(chapter_id)
        return [[[exercise.id, exercise.title, exercise.difficulty] for exercise in exercises], gr.update(value="请选择一个习题"), gr.update(value=""), gr.update(value="")]

    def _handle_exercise_select(self, evt: gr.SelectData):
        """处理习题选择"""
        if evt.index[1] != 0:
            return gr.update()
        exercise_id = evt.value
        LOG.info(f"Selecting exercise: {exercise_id}")
        exercise = self.exercise_service.get_exercise_by_id(exercise_id)
        self.current_exercise = exercise
        test_description = f"### 题目：{exercise.id}. {exercise.title}\n\n{exercise.description}\n\n"
        for i, test_case in enumerate(exercise.test_cases, 1):
            test_description += f"\n##### case {i}:\n&nbsp;&nbsp;&nbsp;&nbsp;**输入**: {test_case.input}  \n&nbsp;&nbsp;&nbsp;&nbsp;**输出**: {test_case.expected_output}"
        return [test_description, gr.update(value="")]
    
    def _handle_get_solution(self, visible):
        """处理查看答案按钮"""
        if visible:
            return ["", gr.update(visible=False)]
        else:
            solution = self.current_exercise.solution
            return [f"```c\n{solution}\n```", gr.update(visible=True)]

    def _get_ai_feedback_start(self):
        return "*AI 分析中...*"
    
    async def _get_ai_feedback(self, exercise_description: str, input_data: str, code: str, output: str):
        """处理AI分析按钮"""
        async for analysis in self.feedback_service.get_feedback(code=code, compile_result=output, input_data=input_data, exercise_description=exercise_description):
            yield analysis
    
    async def _run_code(self, code: str, input_data: str):
        """处理代码运行"""
        if not self.current_exercise:
            LOG.warning("Attempted to run code without selecting an exercise")
            return "请先选择一个习题"
        
        LOG.info(f"Running code for exercise: {self.current_exercise}")
        result = await self.compiler_service.compile_and_run(code, input_data)
        return result["output"]
            
    
    def _clean_code(self):
        return [
            gr.update(value=""),
            gr.update(value=""),
            gr.update(value=""),
        ]
    
    def create(self):
        """创建习题练习标签页"""
        with gr.Tab("习题练习✍️"):
            with gr.Column(elem_classes=["exercise-container"]):
                # 提示信息
                gr.Markdown(
                    "> 💡 提示：配置 API Key 后可启用 AI 分析功能，获得更专业的代码建议，让你的学习事半功倍！")
                
                # 章节和习题列表
                with gr.Column(elem_classes=["exercise-card"]):
                    chapter_radio = gr.Radio(
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
                        elem_classes=["exercise-list"],
                        max_height=300,
                    )
                
                # 习题详情和代码编辑器
                with gr.Row():
                    with gr.Column(scale=2):
                        exercise_description = gr.Markdown(
                            "请选择一个习题",
                            max_height=500,
                            show_copy_button=True,
                            elem_classes=["exercise-description"]
                        )
                        
                        solution_area = gr.Markdown(
                            # height=100,
                            max_height=500,
                            elem_classes=["solution-area"]
                        )
                        
                        with gr.Row(elem_classes=["button-group"]):
                            get_solution_button = gr.Button(
                                "💡 查看/隐藏答案",
                                variant="secondary",
                            )
                            get_ai_feedback_button = gr.Button(
                                "🤖 AI 分析",
                                variant="primary",
                            )
                        
                        ai_feedback = gr.Markdown(
                            show_copy_button=True, 
                            elem_classes=["ai-feedback"],
                            max_height=500,
                        )
                        
                    with gr.Column(scale=3, elem_classes=["code-card"]):
                        
                        code_editor = gr.Code(
                            language="c",
                            label="编写代码",
                            lines=20,
                            max_lines=50,
                            elem_classes=["code-editor"]
                        )

                        program_input = gr.Textbox(
                            label="程序输入（在这里一次性输出程序运行时需要的所有输入值）",
                            placeholder="多个输入值请用空格分隔，例如: 1 2 3",
                            lines=2,
                        )
                        
                        with gr.Row(elem_classes=["button-group"]):
                            run_btn = gr.Button("▶ 运行", variant="primary")
                            clean_btn = gr.Button("🗑 清空")
                        
                        output_box = gr.Textbox(
                            label="运行结果",
                            lines=5,
                            placeholder="运行结果将显示在这里",
                            interactive=False,
                            elem_classes=["output-box"]
                        )
                        
                    
            # 事件绑定
            chapter_radio.change(
                fn=self._handle_chapter_select,
                inputs=[chapter_radio],
                outputs=[exercise_list, exercise_description, solution_area, ai_feedback]
            )
            
            exercise_list.select(
                fn=self._handle_exercise_select,
                outputs=[exercise_description, solution_area]
            )
            
            run_btn.click(
                fn=self._run_code,
                inputs=[code_editor, program_input],
                outputs=[output_box],
            )

            get_solution_button.click(
                fn=self._handle_get_solution,
                inputs=[solution_area],
                outputs=[solution_area, solution_area],
            )

            get_ai_feedback_button.click(
                fn=self._get_ai_feedback_start,
                outputs=[ai_feedback]
            ).then(
                fn=self._get_ai_feedback,
                inputs=[exercise_description, program_input, code_editor, output_box],
                outputs=[ai_feedback]
            )

            clean_btn.click(
                fn=self._clean_code,
                outputs=[code_editor, program_input, output_box]
            )