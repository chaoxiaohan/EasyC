# CompilerTab 类文档

## 文件位置
`src/frontend/tabs/compiler_tab.py`

## 功能概述
`CompilerTab` 类用于创建一个代码编译的用户界面，提供代码编辑、编译运行和 AI 分析功能。该类使用 Gradio 库构建界面，并与后端的 `LocalCompilerService` 和 `AIFeedbackService` 进行交互。

## 类结构
### 主要依赖
- `gradio`: 用于构建用户界面
- `time`: 用于处理延时操作
- `backend.compiler.local_compiler_service`: 提供编译服务
- `backend.ai.feedback_service`: 提供 AI 反馈服务

### 初始化方法
```python
def __init__(self, compiler_service: LocalCompilerService, feedback_service: AIFeedbackService):
```
- 参数:
    - `compiler_service`: 编译服务实例
    - `feedback_service`: AI 反馈服务实例

### 私有方法
**_hide_status**
```python
def _hide_status(self):
```
- 功能:
    - 延时 3 秒后隐藏状态提示

**_clean_feedback**
```python
def _clean_feedback(self):
```
- 功能:
    - 重置 AI 反馈文本为默认提示
- 返回:
    - 默认提示文本 "*点击按钮开始分析*"

**_run_code**
```python
async def _run_code(self, code: str, input_data: str):
```
- 参数:
    - `code`: 用户输入的代码
    - `input_data`: 程序输入数据
- 功能:
    - 异步调用编译服务运行代码
- 返回:
    - 包含运行结果的元组

**_get_ai_feedback_start**
```python
def _get_ai_feedback_start(self):
```
- 功能:
    - 显示 AI 分析进行中的提示
- 返回:
    - 提示文本 "*AI 分析中...*"

**_get_ai_feedback**
```python
async def _get_ai_feedback(self, code: str, output: str, input_data: str):
```
- 参数:
    - `code`: 用户代码
    - `output`: 运行结果
    - `input_data`: 程序输入
- 功能:
    - 异步获取 AI 分析反馈

**_clean_code**
```python
def _clean_code(self):
```
- 功能:
    - 清空所有输入和输出区域
- 返回:
    - 包含三个 gr.update 对象的列表

### 公共方法
**create**
```python
def create(self):
```
- 功能:
    - 创建完整的编译界面
    - 设置 UI 组件和事件处理
- 主要组件:
    1. 代码编辑区域 (左侧)
       - C 代码编辑器
       - 程序输入框
       - 运行和清空按钮
    2. 输出区域 (右侧)
       - 运行结果显示
       - AI 分析按钮
       - AI 反馈显示

### UI 布局
```
在线编译⚡
├── 提示信息
└── 主界面
    ├── 左侧编辑区 (3/5宽度)
    │   ├── 代码编辑器 (15行)
    │   ├── 程序输入框 (2行)
    │   └── 按钮组
    │       ├── 运行按钮
    │       └── 清空按钮
    └── 右侧输出区 (2/5宽度)
        ├── 运行结果框 (6行)
        ├── AI分析按钮
        └── AI反馈显示区
```

### 事件处理
1. **运行按钮点击**:
   - 清空旧的 AI 反馈
   - 执行代码并显示结果

2. **AI分析按钮点击**:
   - 显示分析中提示
   - 获取并显示 AI 反馈

3. **清空按钮点击**:
   - 清空所有输入和输出区域

### 使用示例
```python
compiler_service = LocalCompilerService()
feedback_service = AIFeedbackService()
compiler_tab = CompilerTab(compiler_service, feedback_service)
tab = compiler_tab.create()
```

### 注意事项
- 所有代码运行和 AI 分析操作都是异步的
- UI 组件使用了自定义的 CSS 类进行样式控制
- 运行结果和 AI 反馈都支持复制功能