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
- **AIFeedbackEngine**: 底层的AI引擎实现，直接与DeepSeek API交互
- **AIFeedbackService**: 上层服务封装，提供友好的接口给其他模块使用

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
3. API密钥可以通过 `update_api_key` 方法动态更新