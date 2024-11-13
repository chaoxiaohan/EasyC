# ExerciseService 类设计文档

## 功能概述
`ExerciseService` 类是习题模块的核心服务层，负责协调习题数据访问和代码运行功能，提供高层业务逻辑实现。

## 类结构
```python
class ExerciseService:
    def __init__(self, compiler_service)
    def get_chapters(self) -> List[dict]
    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]
    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]
    async def run_code(self, exercise_id: str, code: str) -> dict
```

## 核心功能

### 1. 初始化
- **方法**: `__init__(compiler_service)`
- **功能**: 
  - 初始化习题仓库
  - 注入编译器服务依赖
- **依赖**:
  - ExerciseRepository
  - CompilerService

### 2. 数据访问
- **方法组**:
  - `get_chapters()`
  - `get_exercises_by_chapter()`
  - `get_exercise_by_id()`
- **功能**:
  - 提供习题数据的高层访问接口
  - 封装仓库层的数据操作
  - 提供类型安全的返回值

### 3. 代码运行
- **方法**: `run_code(exercise_id: str, code: str)`
- **功能**:
  - 验证习题存在性
  - 运行用户代码
  - 处理运行结果
- **返回格式**:
  ```python
  {
      "status": "success/error",
      "output": "运行输出",
      "error": "错误信息"
  }
  ```

## 错误处理
- 习题不存在时返回错误信息
- 代码运行错误时包装异常信息
- 使用日志记录关键操作

## 异步处理
- 代码运行采用异步方式
- 支持并发请求处理
- 避免阻塞主线程

## 扩展性考虑
- 支持后续添加更多测试用例
- 预留 AI 反馈接口
- 支持添加用户进度追踪

## 使用示例
```python
# 初始化服务
compiler_service = CompilerService()
exercise_service = ExerciseService(compiler_service)

# 获取习题
chapters = exercise_service.get_chapters()
exercises = exercise_service.get_exercises_by_chapter("chapter1")

# 运行代码
result = await exercise_service.run_code("ex1_1", "user_code")
```