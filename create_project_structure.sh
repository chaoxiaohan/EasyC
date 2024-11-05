#!/bin/bash

# Create root directory
mkdir -p EasyC

# Create main project structure
cd EasyC
mkdir -p backend/compiler backend/exercises backend/ai \
         frontend/static frontend/templates \
         core/models core/services \
         config \
         tests

# Create __init__.py files
touch backend/__init__.py \
      backend/compiler/__init__.py \
      backend/exercises/__init__.py \
      backend/ai/__init__.py \
      frontend/__init__.py \
      core/__init__.py \
      core/models/__init__.py \
      core/services/__init__.py \
      config/__init__.py \
      tests/__init__.py

# Create backend files
cat > backend/compiler/compiler_interface.py << 'EOF'
from abc import ABC, abstractmethod

class CompilerInterface(ABC):
    @abstractmethod
    async def compile_and_run(self, code: str, test_cases: list = None) -> dict:
        """
        Compile and run C code
        Returns: {
            'success': bool,
            'output': str,
            'errors': list,
            'execution_time': float
        }
        """
        pass
EOF

cat > backend/compiler/docker_compiler.py << 'EOF'
from .compiler_interface import CompilerInterface
import docker

class DockerCompiler(CompilerInterface):
    def __init__(self):
        self.client = docker.from_client()
        self.container_config = {
            'image': 'gcc:latest',
            'memory': '50m',
            'cpu_period': 100000,
            'cpu_quota': 50000
        }

    async def compile_and_run(self, code: str, test_cases: list = None) -> dict:
        try:
            # Implementation for Docker-based compilation
            pass
        except Exception as e:
            return {
                'success': False,
                'output': '',
                'errors': [str(e)],
                'execution_time': 0
            }
EOF

cat > backend/exercises/exercise_manager.py << 'EOF'
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
EOF

# Create core model files
cat > core/models/exercise.py << 'EOF'
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
EOF

# Create other necessary files
touch backend/ai/feedback_engine.py \
      backend/ai/code_analyzer.py \
      frontend/views.py \
      core/models/user.py \
      core/models/submission.py \
      core/services/auth_service.py \
      core/services/progress_service.py \
      config/settings.py \
      config/constants.py \
      tests/test_compiler.py \
      tests/test_exercises.py \
      requirements.txt \
      main.py

# Make the script executable
chmod +x create_project_structure.sh

echo "Project structure created successfully!"