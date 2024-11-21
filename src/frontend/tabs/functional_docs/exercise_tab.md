# ExerciseTab 类设计文档

## 功能概述
`ExerciseTab` 类实现了习题练习的用户界面，提供习题选择、代码编辑、运行以及 AI 分析等功能的完整交互界面。

## 类结构
### 主要依赖
- `gradio`: 用于构建用户界面
- `utils.logger`: 日志记录
- `backend.compiler.local_compiler_service`: 编译服务
- `backend.exercise.exercise_service`: 习题服务
- `backend.ai.feedback_service`: AI 反馈服务

### 初始化方法
```python
def __init__(self, exercise_service: ExerciseService, compiler_service: LocalCompilerService, feedback_service: AIFeedbackService):
```
- 参数:
    - `exercise_service`: 习题服务实例
    - `compiler_service`: 编译服务实例
    - `feedback_service`: AI 反馈服务实例

### 私有方法
**_handle_chapter_select**
```python
def _handle_chapter_select(self, chapter_id: str):
```
- 功能: 处理章节选择
- 返回: 更新习题列表和重置相关显示区域

**_handle_exercise_select**
```python
def _handle_exercise_select(self, evt: gr.SelectData):
```
- 功能: 处理习题选择
- 返回: 更新习题描述和清空答案区域

**_handle_get_solution**
```python
def _handle_get_solution(self):
```
- 功能: 获取并显示习题答案
- 返回: 格式化的答案代码

**_get_ai_feedback_start/_get_ai_feedback**
```python
def _get_ai_feedback_start(self)
async def _get_ai_feedback(self, exercise_description: str, input_data: str, code: str, output: str)
```
- 功能: 处理 AI 分析请求
- 返回: AI 分析结果

**_run_code**
```python
async def _run_code(self, code: str, input_data: str):
```
- 功能: 运行用户代码
- 返回: 运行结果

**_clean_code**
```python
def _clean_code(self):
```
- 功能: 清空代码相关输入输出
- 返回: 更新多个组件状态

## UI 布局
```
习题练习✍️
├── 提示信息
├── 习题选择区域
│   ├── 章节选择 (Radio)
│   └── 习题列表 (Dataframe)
└── 主要内容区域 (Row)
    ├── 左侧面板 (Column, scale=2)
    │   ├── 习题描述 (Markdown)
    │   ├── 答案区域 (Markdown)
    │   ├── 按钮组
    │   │   ├── 查看答案按钮
    │   │   └── AI分析按钮
    │   └── AI反馈区域 (Markdown)
    └── 右侧面板 (Column, scale=3)
        ├── 程序输入框 (Textbox)
        ├── 代码编辑器 (Code)
        ├── 按钮组
        │   ├── 运行按钮
        │   └── 清空按钮
        └── 输出框 (Textbox)
```

## 事件处理
1. **章节选择**:
   - 更新习题列表
   - 重置习题描述、答案和 AI 反馈

2. **习题选择**:
   - 更新习题描述
   - 清空答案区域

3. **代码运行**:
   - 执行代码并显示结果

4. **查看答案**:
   - 显示当前习题的答案代码

5. **AI 分析**:
   - 显示分析中状态
   - 获取并显示 AI 反馈

6. **清空代码**:
   - 清空代码编辑器、输入框和输出框

## 使用示例
```python
exercise_service = ExerciseService()
compiler_service = LocalCompilerService()
feedback_service = AIFeedbackService()
exercise_tab = ExerciseTab(exercise_service, compiler_service, feedback_service)
tab = exercise_tab.create()
```

## 注意事项
- 所有代码运行和 AI 分析操作都是异步的
- 使用自定义 CSS 类进行样式控制
- 习题描述和 AI 反馈支持复制功能
- 需要选择习题后才能运行代码
- 完整的日志记录支持