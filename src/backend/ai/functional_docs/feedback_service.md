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
def __init__(self):
```
- 功能:
    - 初始化 `engine` 属性为 None
    - 记录服务初始化日志

### 主要方法
**update_credentials**
```python
def update_credentials(self, api_key: str) -> bool:
```
- 参数:
    - `api_key`: DeepSeek API密钥
- 功能:
    - 更新API密钥
    - 创建新的 `AIFeedbackEngine` 实例
- 返回值: 
    - `bool`: 更新是否成功
- 特殊情况:
    - 当 `api_key` 为空时，将 `engine` 设为 None 并返回 True

**get_feedback**
```python
async def get_feedback(self, code: str, compile_result: dict, input_data: str=None, exercise_description: str=None) -> str:
```
- 参数:
    - `code`: 需要反馈的代码
    - `compile_result`: 编译结果的字典
    - `input_data`: 输入数据（可选）
    - `exercise_description`: 练习描述（可选）
- 功能:
    - 检查 engine 是否已初始化
    - 整合所有信息生成 AI 反馈
    - 记录获取反馈的日志
- 返回值: 
    - AI 生成的反馈内容
    - 如果未配置 API Key，返回提示信息
    - 如果发生错误，返回友好的错误信息

### 使用示例
```python
# 初始化服务
service = AIFeedbackService()

# 更新凭证
success = service.update_credentials("your_api_key")

# 获取反馈
try:
    feedback = await service.get_feedback(
        code="your_code_here",
        compile_result={"result": "success"},
        input_data="test input",
        exercise_description="练习描述"
    )
    print(feedback)
except Exception as e:
    print(f"Error: {e}")
```