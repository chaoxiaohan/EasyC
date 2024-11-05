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
