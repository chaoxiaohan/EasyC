# ExerciseRepository 类设计文档

## 功能概述
`ExerciseRepository` 类负责习题数据的存储和访问管理，实现了习题数据的加载、缓存和检索功能。

## 类结构
```python
class ExerciseRepository:
    def __init__(self)
    def _load_exercises(self)
    def get_exercises_by_chapter(self, chapter_id: str) -> List[Exercise]
    def get_exercise_by_id(self, exercise_id: str) -> Optional[Exercise]
```

## 核心功能

### 1. 数据加载
- **方法**: `_load_exercises()`
- **功能**: 从JSON文件加载习题数据到内存
- **实现细节**:
  - 从 index.json 加载章节索引
  - 遍历每个章节的 metadata.json 文件
  - 加载每个章节中的所有习题
  - 将习题数据转换为 Exercise 对象
  - 构建章节缓存数据结构
- **数据流程**:
  1. 加载章节索引
  2. 遍历章节加载元数据
  3. 加载具体习题数据
  4. 构建章节缓存

### 2. 章节管理
- **数据结构**:
  - `_chapter_cache`: 列表类型，存储章节信息和习题数量
  - 格式:
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
    - 返回指定章节的所有习题列表
    - 包含详细的日志记录
  - `get_exercise_by_id(exercise_id: str)`
    - 根据ID获取具体习题
    - 不存在时返回None
    - 包含警告日志记录

## 数据结构
- **主要存储**:
  - `exercises`: 字典类型，键为习题ID，值为Exercise对象
  - `_chapter_cache`: 列表类型，存储章节信息和习题数量
- **数据模型**:
  - Exercise类: 存储习题完整信息
  - TestCase类: 管理测试用例数据

## 错误处理
- FileNotFoundError: 文件不存在时的处理
- JSONDecodeError: JSON解析错误处理
- 通用异常处理
- 所有错误都通过LOG记录详细信息

## 性能优化
- 使用字典结构实现O(1)的习题查询
- 预先构建章节缓存，避免重复计算
- 一次性加载所有数据到内存
- 使用集合(set)存储章节习题ID关系

## 文件结构要求
```
src/data/zero_basis/
├── index.json                # 章节索引文件
├── chapter1/
│   ├── metadata.json        # 章节元数据
│   ├── exercise1.json       # 习题数据
│   └── exercise2.json
└── chapter2/
    ├── metadata.json
    └── ...
```