# EasyC 项目功能概述

## 项目结构
```
src/
├── backend/               # 后端模块
│   ├── ai/               # AI 服务模块
│   ├── compiler/         # 编译服务模块
│   └── exercise/         # 习题系统模块
│
├── frontend/             # 前端模块
│   ├── static/          # 静态资源
│   │   └── css/         # 样式文件
│   └── tabs/            # 界面标签页
│       ├── welcome_tab.py    # 欢迎页
│       ├── compiler_tab.py   # 编译器页
│       ├── exercise_tab.py   # 习题页
│       └── settings_tab.py   # 设置页
│
├── utils/               # 通用工具模块
├── main.py             # 主程序入口
└── functional_docs/    # 功能文档目录
```

## 系统架构
### 整体架构
```
EasyC
├── Frontend Layer (Gradio)
│   ├── Welcome Tab (欢迎页面)
│   ├── Exercise Tab (习题练习)
│   ├── Compiler Tab (在线编译)
│   └── Settings Tab (系统设置)
│
├── Backend Layer
│   ├── Exercise Service
│   │   └── Exercise Repository
│   ├── Compiler Service
│   └── AI Feedback Service
│       └── DeepSeek API Integration
│
└── Utils Layer
    ├── Logger
    └── Path Utils
```

### 数据流
```
用户界面
   ↓
功能路由
   ├── 习题系统 → 习题数据 → 答案验证
   ├── 编译服务 → 编译结果 → 执行输出
   └── AI 分析  → API 调用 → 反馈结果
   ↓
结果展示
```

## 核心功能
1. **习题练习系统**
   - 章节化习题管理
   - 代码验证和评测
   - 答案查看功能
   - 学习进度跟踪

2. **在线编译环境**
   - C 语言代码编辑
   - 实时编译执行
   - 输入输出支持
   - 运行结果展示

3. **AI 代码分析**
   - 代码质量评估
   - 优化建议生成
   - 错误诊断反馈
   - 学习指导建议

4. **系统设置**
   - AI 功能配置
   - API 密钥管理
   - 界面定制选项

## 技术栈
### 后端技术
- Python 3.10+
- asyncio
- DeepSeek Chat API
- GCC 编译器

### 前端技术
- Gradio
- CSS3 (模块化样式)
- Markdown 渲染

### 工具支持
- loguru (日志管理)
- python-dotenv (环境配置)
- pathlib (路径处理)

## 模块职责
### Backend 模块
- 习题数据管理
- 代码编译执行
- AI 服务集成
- 数据缓存优化

### Frontend 模块
- 标签页管理
- 响应式布局
- 主题样式
- 交互处理

### Utils 模块
- 日志系统
- 路径管理
- 配置加载

## 配置要求
1. **环境要求**
   - Python 3.10+
   - GCC 编译器
   - 操作系统：Linux/Windows/MacOS

2. **API 配置**
   - DeepSeek API 密钥
   - 环境变量配置

3. **系统配置**
   - 日志目录权限
   - 临时文件目录
   - 网络访问权限

## 部署指南
1. **环境准备**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux
   pip install -r requirements.txt
   ```

2. **配置设置**
   ```bash
   cp .env.example .env
   # 编辑 .env 文件设置必要的配置
   ```

3. **启动服务**
   ```bash
   python src/main.py
   ```

## 开发指南
### 代码规范
1. **Python 规范**
   - PEP 8 编码规范
   - 类型注解
   - 异步编程规范

2. **CSS 规范**
   - 模块化组织
   - 语义化命名
   - 响应式设计

3. **文档规范**
   - 功能文档
   - API 文档
   - 使用示例

## 维护指南
1. **日常维护**
   - 日志监控
   - 性能优化
   - 错误处理

2. **版本更新**
   - 依赖管理
   - 功能迭代
   - 文档更新

## 注意事项
1. **安全性**
   - API 密钥保护
   - 代码执行隔离
   - 输入验证

2. **性能优化**
   - 异步操作管理
   - 缓存策略
   - 资源控制

3. **可维护性**
   - 模块化设计
   - 代码注释
   - 测试覆盖