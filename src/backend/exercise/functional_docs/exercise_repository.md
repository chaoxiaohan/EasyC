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
  - 使用 ProjectPaths 工具类定位数据文件
  - 解析 JSON 格式的习题数据
  - 将数据转换为 Exercise 对象
  - 使用习题ID作为键进行存储

### 2. 章节管理
- **方法**: `get_chapters()`
- **功能**: 获取所有章节信息及其习题数量
- **返回格式**:
  ```python
  [
      {
          "id": "chapter1",
          "exercise_count": 5
      },
      ...
  ]
  ```

### 3. 习题检索
- **方法**: 
  - `get_exercises_by_chapter(chapter_id: str)`
  - `get_exercise_by_id(exercise_id: str)`
- **功能**:
  - 按章节获取习题列表
  - 根据ID获取具体习题

## 数据结构
- 内部使用字典存储习题数据
- 键: 习题ID
- 值: Exercise 对象实例

## 错误处理
- 文件不存在时抛出异常
- JSON解析错误时记录日志
- 习题ID不存在时返回None

## 性能考虑
- 使用内存缓存提高访问速度
- 避免重复加载数据
- 使用高效的数据结构进行检索