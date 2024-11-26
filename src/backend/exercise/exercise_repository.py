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
        """从多个JSON文件加载习题数据"""
        LOG.info("Loading exercises from JSON files")
        index_path = ProjectPaths.get_project_path('src', 'data', 'zero_basis', 'index.json')
        try:
            # 首先加载章节索引
            with open(index_path, 'r', encoding='utf-8') as f:
                index_data = json.load(f)

            # 初始化章节缓存数据结构
            chapters = {}
            
            # 遍历每个章节加载详细数据
            for chapter in index_data['chapters']:
                chapter_metadata_path = ProjectPaths.get_project_path('src', 'data', 'zero_basis', 
                                                        chapter['path'], 'metadata.json')
                
                with open(chapter_metadata_path, 'r', encoding='utf-8') as f:
                    chapter_metadata = json.load(f)

                # 初始化当前章节的习题集合
                chapters[chapter_metadata['id']] = {}
                chapters[chapter_metadata['id']]['title'] = chapter_metadata['title']
                chapters[chapter_metadata['id']]['exercises'] = set()
                    
                # 加载章节中的每个练习题
                for ex_meta in chapter_metadata['exercises']:
                    exercise_path = ProjectPaths.get_project_path('src', 'data', 'zero_basis',
                                                                chapter['path'], ex_meta['path'])
                    
                    with open(exercise_path, 'r', encoding='utf-8') as f:
                        ex_data = json.load(f)
                        exercise = Exercise(
                            id=ex_data['id'],
                            chapter_id=chapter['id'],
                            title=ex_data['title'],
                            difficulty=ex_data['difficulty'],
                            description=ex_data['description'],
                            solution_template=ex_data['solution_template'],
                            solution=ex_data['solution'],
                            test_cases=[TestCase(**tc) for tc in ex_data['test_cases']]
                        )
                        self.exercises[ex_data['id']] = exercise
                        chapters[chapter_metadata['id']]['exercises'].add(ex_data['id'])
            
            # 构建章节缓存
            self._chapter_cache = [{"id": k, "title": v['title'], "exercise_count": len(v['exercises'])} for k, v in chapters.items()]          
            LOG.info(f"Successfully loaded {len(self.exercises)} exercises in {len(self._chapter_cache)} chapters")
        except FileNotFoundError as e:
            LOG.error(f"File not found: {str(e)}")
            raise
        except json.JSONDecodeError as e:
            LOG.error(f"Invalid JSON format: {str(e)}")
            raise
        except Exception as e:
            LOG.error(f"Unexpected error while loading exercises: {str(e)}")
            raise

    # def get_chapters(self) -> List[dict]:
    #     """获取所有章节信息"""
    #     if not self._chapter_cache:
    #         LOG.debug("Retrieving chapters information")
    #         chapters = {}
    #         for ex in self.exercises.values():
    #             if ex.chapter_id not in chapters:
    #                 chapters[ex.chapter_id] = set()
    #             chapters[ex.chapter_id].add(ex.id)
    #         self._chapter_cache = [{"id": k, "exercise_count": len(v)} for k, v in chapters.items()]
    #     return self._chapter_cache

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
    
