from typing import List, Optional
from core.models.exercise import Exercise

class ExerciseManager:
    def __init__(self):
        self.exercises = {}

    async def get_exercise(self, exercise_id: str) -> Optional[Exercise]:
        return self.exercises.get(exercise_id)

    async def add_exercise(self, exercise: Exercise) -> bool:
        if exercise.exercise_id in self.exercises:
            return False
        self.exercises[exercise.exercise_id] = exercise
        return True

    async def get_exercises_by_category(self, category: str) -> List[Exercise]:
        return [ex for ex in self.exercises.values() if ex.category == category]
