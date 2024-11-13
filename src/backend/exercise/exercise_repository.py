# src/backend/exercise/exercise_repository.py
import json
from utils.path_utils import ProjectPaths
from utils.logger import logger
from typing import List, Optional
from .models.exercise import Exercise, TestCase

class ExerciseRepository:
    def __init__(self):
        self.exercises = {}
        self._load_exercises()

    def _load_exercises(self):
        """从JSON文件加载习题数据"""
        exercises_path = ProjectPaths.get_project_path('src', 'data', 'exercises', 'metadata.json')
        with open(exercises_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for chapter in data['chapters']:
            for ex in chapter['exercises']:
                exercise = Exercise(
                    id=ex['id'],
                    chapter_id=chapter['id'],
                    title=ex['title'],
                    difficulty=ex['difficulty'],
                    description=ex['description'],
                    solution_template=ex['solution_template'],
                    test_cases=[TestCase(**tc) for tc in ex['test_cases']]
                )
                self.exercises[ex['id']] = exercise

    def get_chapters(self) -> List[dict]:
        """获取所有章节信息"""
        chapters = {}
        for ex in self.exercises.values():
            if ex.chapter_id not in chapters:
                chapters[ex.chapter_id] = set()
            chapters[ex.chapter_id].add(ex.id)
        return [{"id": k, "exercise_count": len(v)} for k, v in chapters.items()]

    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]:
        """获取指定章节的所有习题"""
        return [ex for ex in self.exercises.values() if ex.chapter_id == chapter_id]

    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        """根据ID获取习题"""
        return self.exercises.get(exercise_id)