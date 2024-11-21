# src/backend/exercise/models/solution.py
class Solution:
    exercise_id: str
    user_code: str
    status: str  # 'pending', 'passed', 'failed'
    test_results: List[TestResult]
    ai_feedback: str


