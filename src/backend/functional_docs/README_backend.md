# Backend 模块功能概述

## 目录结构
```
backend/
├── ai/                     # AI相关功能模块
│   ├── feedback_engine.py
│   ├── feedback_service.py
│   └── functional_docs/
│
├── compiler/               # 编译相关功能模块
│   ├── local_compiler_service.py
│   └── functional_docs/
│
├── exercise/              # 习题相关功能模块
│   ├── exercise_repository.py
│   ├── exercise_service.py
│   ├── models/
│   │   ├── exercise.py
│   │   └── solution.py
│   └── functional_docs/
│
├── utils/                  # 工具类模块
│   ├── logger.py          # 日志工具
│   └── path_utils.py      # 路径处理工具
│
└── functional_docs/        # 功能文档目录
```

## 模块功能
Backend 模块是整个项目的服务端核心，主要提供以下功能：

1. **代码处理**
   - 代码编译和执行
   - 编译结果收集和处理
   - 运行时环境管理

2. **AI 服务**
   - 代码分析和反馈生成
   - AI API 集成和管理
   - 反馈结果处理

3. **习题管理**
   - 习题数据存储和访问
   - 章节管理
   - 代码运行和验证

4. **工具支持**
   - 日志记录和管理
   - 文件路径处理
   - 通用工具函数

## 核心组件关系
```
Backend
├── LocalCompilerService
│   └── AIFeedbackService
│       └── AIFeedbackEngine
├── ExerciseService
│   └── ExerciseRepository
└── Utils
    ├── Logger
    └── PathUtils
```

## 技术栈
- Python 3.10+
- asyncio 用于异步操作
- DeepSeek Chat API
- 本地编译工具链

## 配置要求
1. **环境配置**
   - Python 运行环境
   - 本地编译器
   - 适当的文件系统权限

2. **API 配置**
   - DeepSeek API 密钥
   - API 配置文件

3. **日志配置**
   - 日志级别设置
   - 日志存储路径

## 数据流
```
用户代码 -> LocalCompilerService
           ├── 编译执行 -> 编译结果
           └── AIFeedbackService
               └── 生成反馈 -> 反馈结果
```

## 错误处理
1. 所有模块都实现了完整的错误处理机制
2. 错误信息会被记录到日志系统
3. 用户友好的错误消息会返回给前端

## 扩展性设计
1. **模块化结构**
   - 每个功能模块都是独立的
   - 模块间通过清晰的接口通信

2. **可配置性**
   - 支持不同的编译环境
   - 可切换不同的 AI 服务提供商
   - 可自定义日志配置

3. **可测试性**
   - 模块间低耦合
   - 支持单元测试和集成测试

## 使用注意
1. 确保所有必要的环境依赖已安装
2. API 密钥需要妥善保管和定期更新
3. 定期检查日志文件大小和清理
4. 注意临时文件的管理和清理
5. 监控系统资源使用情况

## 维护建议
1. **日常维护**
   - 定期检查日志
   - 更新 API 密钥
   - 清理临时文件

2. **性能优化**
   - 监控响应时间
   - 优化资源使用
   - 定期检查内存使用

3. **安全性**
   - 定期更新依赖
   - 检查安全漏洞
   - 审查代码执行权限

## 未来规划
1. 支持更多编程语言
2. 集成更多 AI 模型
3. 优化编译性能
4. 增强错误处理机制
5. 添加更多自动化测试