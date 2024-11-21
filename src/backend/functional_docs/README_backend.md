# Backend 模块功能概述

## 目录结构
```
backend/
├── ai/                     # AI相关功能模块
│   ├── feedback_engine.py  # AI引擎实现
│   ├── feedback_service.py # AI服务实现
│   └── functional_docs/    # AI模块文档
│
├── compiler/               # 编译相关功能模块
│   ├── local_compiler_service.py  # 本地编译服务
│   └── functional_docs/    # 编译模块文档
│
├── exercise/              # 习题相关功能模块
│   ├── exercise_repository.py  # 习题数据访问层
│   ├── exercise_service.py    # 习题服务实现
│   ├── models/
│   │   ├── exercise.py      # 习题模型
│   │   └── test_case.py     # 测试用例模型
│   └── functional_docs/     # 习题模块文档
│
├── utils/                  # 工具类模块
│   ├── logger.py          # 日志工具
│   └── path_utils.py      # 路径处理工具
│
└── functional_docs/        # 功能文档目录
```

## 模块功能
Backend 模块是整个项目的服务端核心，主要提供以下功能：

1. **代码编译与执行**
   - 本地代码编译和运行
   - 安全的执行环境管理
   - 超时和资源限制控制
   - 标准化的执行结果处理

2. **AI 反馈服务**
   - DeepSeek Chat API 集成
   - 代码分析和反馈生成
   - API 凭证管理
   - 异步反馈处理

3. **习题系统**
   - 高效的习题数据管理
   - 章节组织和缓存
   - 异步代码验证
   - O(1)复杂度的数据访问

4. **工具支持**
   - 统一的日志记录
   - 文件路径处理
   - 通用工具函数

## 核心组件关系
```
Backend
├── LocalCompilerService     # 编译和执行代码
│   └── 安全编译选项和超时控制
│
├── AIFeedbackService       # AI反馈生成
│   └── AIFeedbackEngine    # DeepSeek API集成
│
├── ExerciseService        # 习题核心服务
│   ├── ExerciseRepository # 数据访问层
│   └── 高效缓存机制
│
└── Utils
    ├── Logger            # 统一日志工具
    └── PathUtils         # 路径处理工具
```

## 技术特性
1. **异步处理**
   - 使用 asyncio 支持并发
   - 异步代码执行
   - 非阻塞 AI 反馈

2. **性能优化**
   - O(1) 复杂度的数据访问
   - 预构建缓存机制
   - 内存优化的数据结构

3. **安全机制**
   - 代码执行沙箱
   - 编译安全选项
   - API 凭证保护

## 配置要求
1. **环境要求**
   - Python 3.10+
   - GCC 编译器
   - 适当的文件系统权限

2. **API 配置**
   - DeepSeek API 密钥
   - API 配置参数

3. **系统配置**
   - 临时文件目录权限
   - 日志存储路径
   - 编译超时限制

## 错误处理
- 统一的异常捕获机制
- 标准化的错误响应格式
- 详细的日志记录
- 用户友好的错误提示

## 维护指南
1. **日常维护**
   - 检查日志文件
   - 更新 API 凭证
   - 清理临时文件

2. **性能监控**
   - 响应时间监控
   - 内存使用监控
   - 并发请求处理

3. **安全维护**
   - 定期更新依赖
   - 检查编译选项
   - 审查执行权限

## 未来规划
1. 支持更多编程语言
2. 增强 AI 反馈能力
3. 优化缓存机制
4. 增加自动化测试
5. 改进错误处理机制