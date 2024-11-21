# AI 模块功能概述

## 目录结构
```
ai/
├── feedback_engine.py    # AI反馈引擎实现
├── feedback_service.py   # AI反馈服务实现
└── functional_docs/      # 功能文档目录
```

## 模块功能
该模块负责处理所有与AI相关的功能，主要包括：
1. 与DeepSeek Chat API的集成
2. 代码反馈的生成
3. AI服务的状态管理

## 核心组件

### AIFeedbackEngine
底层的AI引擎实现，直接与DeepSeek API交互
- 主要功能：
  - 初始化和管理DeepSeek Chat API连接
  - 加载和使用提示模板
  - 处理AI对话请求
- 关键方法：
  - `__init__(model: str, api_key: str)`: 初始化引擎
  - `chat(message)`: 发送消息并获取AI响应

### AIFeedbackService
上层服务封装，提供友好的接口给其他模块使用
- 主要功能：
  - 管理AI引擎的生命周期
  - 提供异步反馈生成接口
  - 处理凭证更新
- 关键方法：
  - `update_credentials(api_key: str) -> bool`: 更新API凭证
  - `get_feedback(code: str, compile_result: dict, input_data: str, exercise_description: str) -> str`: 获取AI反馈

## 依赖关系
```
AIFeedbackService
    └── AIFeedbackEngine
        └── DeepSeek Chat API
```

## 配置要求
- 需要有效的DeepSeek API密钥
- 需要提示模板文件 (`result_feedback_prompt.txt`)

## 使用注意
1. 所有API调用都有错误处理和日志记录
2. 服务初始化时可以不提供API密钥，但某些功能将不可用
3. API密钥可以通过 `update_credentials` 方法动态更新
4. 反馈生成支持以下参数：
   - 代码内容
   - 编译结果
   - 输入数据（可选）
   - 练习描述（可选）

## 错误处理
- API密钥无效时的友好提示
- API调用失败时的错误信息
- 服务不可用时的状态提示

## 日志记录
- 使用统一的日志工具 (`utils.logger`)
- 记录所有关键操作和错误信息
- 支持调试级别的详细日志