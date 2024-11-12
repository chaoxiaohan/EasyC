# Compiler 模块功能概述

## 目录结构
```
compiler/
├── local_compiler_service.py    # 本地编译服务实现
└── functional_docs/             # 功能文档目录
```

## 模块功能
该模块负责处理所有与代码编译和执行相关的功能，主要包括：
1. 本地代码编译
2. 代码执行和结果收集
3. 编译环境管理
4. 与AI反馈服务的集成

## 核心组件
- **LocalCompilerService**: 提供本地编译和执行服务，包括代码编译、运行和结果处理

## 依赖关系
```
LocalCompilerService
    ├── 系统编译器
    └── AIFeedbackService (可选)
```

## 配置要求
- 需要本地编译环境
- 需要适当的文件系统权限
- 可选：DeepSeek API密钥（用于AI反馈功能）

## 使用注意
1. 编译和执行过程有完整的错误处理和日志记录
2. 支持异步操作
3. 临时文件会自动创建和清理
4. AI反馈功能需要有效的API密钥