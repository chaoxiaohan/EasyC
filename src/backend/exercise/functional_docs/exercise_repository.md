# ExerciseRepository 类设计文档

## 功能概述
`ExerciseRepository` 类负责习题数据的存储和访问管理，实现了习题数据的加载、缓存和检索功能。

## 类结构
```python
class ExerciseRepository:
    def __init__(self)
    def _load_exercises(self)
    def get_chapters(self) -> List[dict]
    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]
    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]
```

## 核心功能

### 1. 数据加载
- **方法**: `_load_exercises()`
- **功能**: 从JSON文件加载习题数据到内存
- **实现细节**:
  - 使用 ProjectPaths 工具类定位数据文件 (metadata.json)
  - 解析 JSON 格式的习题数据
  - 将数据转换为 Exercise 对象，包含完整的测试用例信息
  - 使用习题ID作为键进行存储
  - 详细的错误日志记录

### 2. 章节管理
- **方法**: `get_chapters()`
- **功能**: 获取所有章节信息及其习题数量
- **实现细节**:
  - 使用章节缓存（_chapter_cache）提高性能
  - 动态计算每个章节的习题数量
- **返回格式**:
  ```python
  [
      {
          "id": "chapter_id",
          "exercise_count": number_of_exercises
      },
      ...
  ]
  ```

### 3. 习题检索
- **方法**: 
  - `get_exercises_by_chapter(chapter_id: str)`
  - `get_exercise_by_id(exercise_id: str)`
- **功能**:
  - 按章节获取习题列表，返回该章节的所有Exercise对象
  - 根据ID获取具体习题，不存在时返回None
- **日志记录**:
  - 包含详细的调试日志，记录检索操作和结果

## 数据结构
- **主要存储**:
  - `exercises`: 字典类型，键为习题ID，值为Exercise对象
  - `_chapter_cache`: 字典类型，存储章节信息缓存
- **数据模型**:
  - 使用Exercise类存储习题信息
  - 包含TestCase类管理测试用例

## 错误处理
- FileNotFoundError: 习题元数据文件不存在
- JSONDecodeError: JSON格式解析错误
- 通用异常处理并记录详细错误信息
- 所有错误都通过日志系统记录

## 性能优化
- 使用章节信息缓存机制
- 一次性加载所有习题数据到内存
- 使用字典结构实现O(1)的习题查询
- 避免重复计算章节信息