# src/backend/exercise/exercise_service.py

from utils.logger import LOG
from typing import List, Optional
from .exercise_repository import ExerciseRepository
from .models.exercise import Exercise

class ExerciseService:
    def __init__(self, compiler_service):
        self.repository = ExerciseRepository()
        self.compiler_service = compiler_service

    def get_chapters(self) -> List[dict]:
        """获取所有章节"""
        return self.repository.get_chapters()

    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]:
        """获取指定章节的习题列表"""
        return self.repository.get_exercises_by_chapter(chapter_id)

    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        """获取指定习题详情"""
        return self.repository.get_exercise_by_id(exercise_id)

    async def run_code(self, exercise_id: str, code: str) -> dict:
        """运行用户代码"""
        exercise = self.repository.get_exercise_by_id(exercise_id)
        if not exercise:
            return {"error": "习题不存在"}

        # 使用第一个测试用例运行代码
        test_case = exercise.test_cases[0]
        result = await self.compiler_service.run(code, test_case.input)
        
        return {
            "status": "success",
            "output": result.output if result.success else result.error,
            "error": None if result.success else result.error
        }