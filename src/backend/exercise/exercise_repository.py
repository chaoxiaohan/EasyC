# src/backend/exercise/exercise_repository.py
import json
from utils.path_utils import ProjectPaths
from utils.logger import LOG
from typing import List, Optional
from .models.exercise import Exercise, TestCase

class ExerciseRepository:
    def __init__(self):
        LOG.info("Initializing ExerciseRepository")
        self.exercises = {}
        self._chapter_cache = {}
        self._load_exercises()

    def _load_exercises(self):
        """从JSON文件加载习题数据"""
        LOG.info("Loading exercises from JSON file")
        exercises_path = ProjectPaths.get_project_path('src', 'data', 'exercises', 'metadata.json')
        
        try:
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
            LOG.info(f"Successfully loaded {len(self.exercises)} exercises")
        except FileNotFoundError:
            LOG.error(f"Exercise metadata file not found at: {exercises_path}")
            raise
        except json.JSONDecodeError:
            LOG.error(f"Invalid JSON format in exercise metadata file: {exercises_path}")
            raise
        except Exception as e:
            LOG.error(f"Unexpected error while loading exercises: {str(e)}")
            raise

    def get_chapters(self) -> List[dict]:
        """获取所有章节信息"""
        if not self._chapter_cache:
            LOG.debug("Retrieving chapters information")
            chapters = {}
            for ex in self.exercises.values():
                if ex.chapter_id not in chapters:
                    chapters[ex.chapter_id] = set()
                chapters[ex.chapter_id].add(ex.id)
            self._chapter_cache = [{"id": k, "exercise_count": len(v)} for k, v in chapters.items()]
        return self._chapter_cache

    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]:
        """获取指定章节的所有习题"""
        LOG.debug(f"Retrieving exercises for chapter: {chapter_id}")
        exercises = [ex for ex in self.exercises.values() if ex.chapter_id == chapter_id]
        LOG.debug(f"Found {len(exercises)} exercises in chapter {chapter_id}")
        return exercises

    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]:
        """根据ID获取习题"""
        exercise = self.exercises.get(exercise_id)
        if exercise:
            LOG.debug(f"Retrieved exercise: {exercise_id}")
        else:
            LOG.warning(f"Exercise not found: {exercise_id}")
        return exercise