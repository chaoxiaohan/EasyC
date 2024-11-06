from datetime import datetime
from typing import List, Dict

class Exercise:
    def __init__(self, 
                 exercise_id: str,
                 title: str,
                 description: str,
                 difficulty: str,
                 category: str,
                 test_cases: List[Dict],
                 template_code: str = ""):
        self.exercise_id = exercise_id
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.category = category
        self.test_cases = test_cases
        self.template_code = template_code
        self.created_at = datetime.utcnow()
