# LocalCompilerService 类文档

## 文件位置
`src/backend/compiler/local_compiler_service.py`

## 功能概述
`LocalCompilerService` 是一个本地编译和运行代码的服务类，负责接收代码并在本地环境中编译和执行。该类提供了编译、运行代码的功能，并能够处理输入数据和返回结果。

## 类结构
### 主要依赖
- `os`: 用于文件和目录操作
- `subprocess`: 用于执行外部命令
- `uuid`: 用于生成唯一文件名
- `typing`: 提供类型提示
- `utils.logger`: 提供日志记录功能
- `backend.ai.feedback_service`: 提供 `AIFeedbackService` 类

### 构造函数
```python
def __init__(self, api_key: str = None):
```
- 参数:
    - `api_key`: 可选的API密钥
- 功能:
    - 初始化编译目录
    - 创建编译目录并记录初始化日志

### 主要方法
**compile_and_run**
```python
async def compile_and_run(self, code: str, input_data: Optional[str] = None) -> Dict:
```
- 参数:
    - `code`: 需要编译和运行的代码
    - `input_data`: 可选的输入数据
- 功能:
    - 编译并运行代码
    - 处理编译和运行的结果
    - 记录编译和运行过程中的日志
- 返回值: 包含成功状态、输出、错误信息和执行时间的字典
- 异常处理: 捕获并记录可能发生的错误，返回用户友好的错误信息

**update_credentials**
```python
def update_credentials(self, api_key: str) -> bool:
```
- 参数:
    - `api_key`: DeepSeek API密钥
- 功能:
    - 更新API密钥并重新初始化反馈服务
- 返回值: 更新成功返回 `True`，失败返回 `False`

**get_ai_feedback**
```python
async def get_ai_feedback(self, code: str, output: dict) -> str:
```
- 参数:
    - `code`: 需要反馈的代码
    - `output`: 编译和运行的结果
- 功能:
    - 获取AI反馈
    - 检查API密钥是否有效
- 返回值: AI生成的反馈内容或错误信息

### 工作流程
1. 初始化时创建编译目录
2. 通过 `compile_and_run` 方法编译和运行代码
3. 通过 `update_credentials` 方法更新API密钥
4. 使用 `get_ai_feedback` 方法获取代码反馈
5. 所有操作都有错误日志记录

### 注意事项
- 需要有效的DeepSeek API密钥以启用AI反馈功能
- 异步方法 `compile_and_run` 和 `get_ai_feedback` 需要在异步上下文中调用
- 所有API调用都有错误处理和日志记录

### 使用示例
```python
# 初始化服务
compiler_service = LocalCompilerService(api_key="your_api_key")

# 编译并运行代码
result = await compiler_service.compile_and_run("print('Hello, World!')", input_data="")

# 更新API密钥
compiler_service.update_credentials("new_api_key")

# 获取反馈
try:
    feedback = await compiler_service.get_ai_feedback("your_code_here", {"result": "success"})
    print(feedback)
except Exception as e:
    print(f"Error: {e}")
``` 