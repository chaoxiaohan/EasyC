# src/backend/exercise/models/exercise.py

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TestCase:
    input: str
    expected_output: str

@dataclass
class Exercise:
    id: str
    chapter_id: str
    title: str
    difficulty: str
    description: str
    solution_template: str
    test_cases: List[TestCase]
