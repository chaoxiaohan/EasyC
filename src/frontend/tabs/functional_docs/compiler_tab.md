# create_compiler_tab 函数文档

## 文件位置
`src/frontend/tabs/compiler_tab.py`

## 功能概述
`create_compiler_tab` 函数用于创建一个代码编译的用户界面，允许用户输入代码、程序输入，并通过按钮执行编译和运行操作。该函数使用 Gradio 库构建界面，并与后端的 `LocalCompilerService` 进行交互。

## 函数结构
### 主要依赖
- `gradio`: 用于构建用户界面
- `time`: 用于处理时间相关的功能
- `pyperclip`: 用于剪贴板操作
- `backend.compiler.local_compiler_service`: 提供 `LocalCompilerService` 类

### 函数参数
```python
def create_compiler_tab(compiler_service: LocalCompilerService):
```
- 参数:
    - `compiler_service`: `LocalCompilerService` 的实例，用于编译和运行代码

### 主要组件
1. **设置面板**
   - 包含 API Key 输入框和保存设置按钮
   - 提供显示和保存设置的功能

2. **代码编辑区域**
   - 包含 C 代码编辑器和程序输入框
   - 提供运行和清空代码的按钮

3. **输出区域**
   - 显示运行结果和 AI 分析反馈
   - 包含复制分析结果的按钮

### 主要方法
**show_settings**
```python
def show_settings():
```
- 功能:
    - 显示 API Key 输入框和保存按钮

**save_settings**
```python
def save_settings(api_key):
```
- 参数:
    - `api_key`: 用户输入的 API Key
- 功能:
    - 更新编译服务的 API Key
    - 隐藏输入框和按钮，显示成功提示

**copy_feedback**
```python
def copy_feedback(markdown_text):
```
- 参数:
    - `markdown_text`: AI 反馈的 Markdown 文本
- 功能:
    - 将反馈内容复制到剪贴板

**hide_status**
```python
def hide_status():
```
- 功能:
    - 隐藏复制状态提示

**clean_feedback**
```python
def clean_feedback():
```
- 功能:
    - 重置 AI 反馈文本

**run_code**
```python
async def run_code(code, input_data):
```
- 参数:
    - `code`: 用户输入的代码
    - `input_data`: 用户输入的程序输入
- 功能:
    - 调用编译服务编译和运行代码
    - 返回运行结果

**get_ai_feedback_start**
```python
def get_ai_feedback_start():
```
- 功能:
    - 显示 AI 分析中提示

**get_ai_feedback**
```python
async def get_ai_feedback(code, output):
```
- 参数:
    - `code`: 用户输入的代码
    - `output`: 运行结果
- 功能:
    - 调用编译服务获取 AI 反馈

### 工作流程
1. 创建 Gradio 界面，包含设置面板、代码编辑区域和输出区域
2. 处理用户输入和按钮点击事件
3. 调用 `LocalCompilerService` 的方法进行代码编译和运行
4. 显示运行结果和 AI 反馈
5. 提供复制和清空功能

### 注意事项
- 确保在使用 AI 反馈功能前已设置有效的 API Key
- 所有异步操作需在支持异步的环境中执行

### 使用示例
```python
# 创建编译标签
create_compiler_tab(compiler_service)
``` 