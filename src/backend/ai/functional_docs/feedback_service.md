# AIFeedbackService 类文档

## 文件位置
`src/backend/ai/feedback_service.py`

## 功能概述
`AIFeedbackService` 是一个AI反馈服务类，负责与 `AIFeedbackEngine` 交互以生成代码反馈。该类提供了API密钥的管理和获取AI反馈的功能。

## 类结构
### 主要依赖
- `json`: 用于处理JSON数据
- `utils.logger`: 提供日志记录功能
- `feedback_engine`: 提供 `AIFeedbackEngine` 类

### 构造函数
```python
def __init__(self, api_key: str=None):
```
- 参数:
    - `api_key`: DeepSeek API密钥，可选
- 功能:
    - 初始化 `AIFeedbackEngine` 实例
    - 记录服务初始化日志

### 主要方法
**update_api_key**
```python
def update_api_key(self, api_key: str):
```
- 参数:
    - `api_key`: DeepSeek API密钥
- 功能:
    - 更新API密钥
    - 更新 `AIFeedbackEngine` 实例中的API密钥

**get_feedback**
```python
async def get_feedback(self, code: str, compile_result: dict) -> str:
```
- 参数:
    - `code`: 需要反馈的代码
    - `compile_result`: 编译结果的字典
- 功能:
    - 生成AI反馈
    - 记录获取反馈的日志
- 返回值: AI生成的反馈内容
- 异常处理: 捕获并记录可能发生的错误，返回用户友好的错误信息

### 工作流程
1. 初始化时创建 `AIFeedbackEngine` 实例
2. 通过 `update_api_key` 方法更新API密钥
3. 使用 `get_feedback` 方法获取代码反馈
4. 所有操作都有错误日志记录

### 注意事项
- 需要有效的DeepSeek API密钥
- 异步方法 `get_feedback` 需要在异步上下文中调用
- 所有API调用都有错误处理和日志记录

### 使用示例
```python
# 初始化服务
service = AIFeedbackService(api_key="your_api_key")

# 更新API密钥
service.update_api_key("new_api_key")

# 获取反馈
try:
    feedback = await service.get_feedback("your_code_here", {"result": "success"})
    print(feedback)
except Exception as e:
    print(f"Error: {e}")
``` 