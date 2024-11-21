# EasyC 🚀

<div align="center">

[English](https://github.com/ophiraShen/EasyC/blob/main/README.md) | 简体中文

[![许可证](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-required-blue.svg)](https://www.docker.com/)

一个直观的、AI驱动的平台，旨在让初学者轻松掌握C语言编程，提升学习体验。
</div>

## 🌟 特性

### 1. 习题练习系统
- 章节化的习题管理
- 实时代码验证
- 答案查看功能
- 学习进度追踪（即将推出）

### 2. 代码编译与执行
- 实时C代码编译
- 交互式代码执行
- 全面的错误处理
- 程序输入/输出支持

### 3. AI驱动分析
- 智能代码审查
- 优化建议
- 错误诊断
- 学习建议

### 4. 用户界面
- 清晰直观的设计
- 实时反馈
- 响应式布局
- 语法高亮

## 🔧 系统架构

```
EasyC
├── 前端 (Gradio)
│   ├── 欢迎页面
│   ├── 习题练习
│   ├── 在线编译
│   └── 系统设置
│
├── 后端服务
│   ├── 习题服务
│   ├── 编译服务
│   └── AI反馈服务
│
└── 工具模块
    ├── 日志系统
    └── 路径管理
```

## 🚀 快速开始

### 使用 Docker（推荐）
```bash
# 克隆仓库
git clone https://github.com/ophiraShen/EasyC.git

# 使用 Docker Compose 启动
docker-compose up --build
```

### 手动安装
```bash
# 克隆仓库
git clone https://github.com/ophiraShen/EasyC.git

# 安装依赖
pip install -r requirements.txt

# 启动应用
python src/main.py
```

## 💻 系统要求

### 环境要求
- Python 3.10+
- GCC 编译器
- Docker（可选）
- DeepSeek API密钥（用于AI功能）

### 依赖项
- Gradio 5.4.0
- Python-dotenv 1.0.1
- Loguru 0.7.2
- 其他依赖见 `requirements.txt`

## 🛠️ 开发指南

### 项目结构
```
src/
├── backend/               # 后端服务
│   ├── ai/               # AI分析
│   ├── compiler/         # 代码编译
│   └── exercise/         # 习题系统
├── frontend/             # 界面组件
│   ├── static/          # 静态资源
│   └── tabs/            # 界面标签页
├── utils/               # 工具模块
└── main.py              # 入口文件
```

### 核心组件
1. **前端模块**
   - 欢迎页面
   - 习题系统
   - 代码编译器
   - 设置管理

2. **后端模块**
   - 习题管理
   - 代码编译
   - AI分析
   - 错误处理

3. **工具模块**
   - 日志系统
   - 路径管理
   - 通用工具

## 📝 文档

详细的模块文档：
- [前端文档](src/frontend/functional_docs/README_frontend.md)
- [后端文档](src/backend/functional_docs/README_backend.md)
- [工具文档](src/utils/functional_docs/README_utils.md)

## 🤝 贡献指南

我们欢迎各种形式的贡献！请查看我们的[贡献指南](CONTRIBUTING.md)。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m '添加了一些很棒的特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 🔒 安全性

- 安全的代码执行环境
- API密钥保护
- 定期安全更新
- 资源使用限制

## 📈 未来规划

1. **功能扩展**
   - 习题进度追踪
   - 多测试用例支持
   - 学习资源集成
   - 代码自动保存功能

2. **技术改进**
   - 并行测试执行
   - 增强AI能力
   - 性能优化
   - 移动端适配

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- DeepSeek团队提供AI能力支持
- GCC团队提供C编译器
- Docker提供容器化支持
- 所有贡献者和支持者

## 📬 联系方式

项目链接：[https://github.com/ophiraShen/EasyC](https://github.com/ophiraShen/EasyC)

---

<p align="center">为热爱C语言编程的学习者们精心打造 ❤️</p>