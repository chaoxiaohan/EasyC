# src/backend/compiler/debugger_interface.py
from abc import ABC, abstractmethod

class DebuggerInterface(ABC):
    @abstractmethod
    async def start_debug_session(self, code: str) -> str:
        """启动调试会话"""
        pass
    
    @abstractmethod
    async def step(self, session_id: str) -> dict:
        """单步执行"""
        pass
    
    @abstractmethod
    async def get_variables(self, session_id: str) -> dict:
        """获取当前变量状态"""
        pass