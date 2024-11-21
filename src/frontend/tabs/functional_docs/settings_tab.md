# SettingsTab 类设计文档

## 文件位置
`src/frontend/tabs/settings_tab.py`

## 功能概述
`SettingsTab` 类实现了应用程序的设置界面，主要用于配置 AI 功能相关的设置，包括 DeepSeek API Key 的管理。

## 类结构
### 主要依赖
- `gradio`: 用于构建用户界面
- `utils.logger`: 日志记录
- `backend.ai.feedback_service`: AI 反馈服务

### 初始化方法
```python
def __init__(self, feedback_service: AIFeedbackService):
```
- 参数:
    - `feedback_service`: AI 反馈服务实例，用于管理 API 凭证

### 私有方法
**_save_settings**
```python
def _save_settings(self, api_key: str):
```
- 功能: 
    - 保存 API Key 设置
    - 更新 AI 反馈服务的凭证
- 参数:
    - `api_key`: DeepSeek API Key
- 返回:
    - 成功时: 显示成功消息
    - 失败时: 显示错误提示
- 日志:
    - 记录设置保存操作

### 公共方法
**create**
```python
def create(self):
```
- 功能:
    - 创建设置界面
    - 设置 UI 组件和事件处理
- 主要组件:
    1. AI 功能配置说明
    2. API Key 输入框
    3. 保存按钮
    4. 状态消息显示

## UI 布局
```
设置 ⚙️
└── 设置容器
    ├── 说明文档 (Markdown)
    │   ├── AI 功能配置说明
    │   └── API Key 获取指南
    ├── API Key 输入框 (Textbox)
    ├── 保存按钮 (Button)
    └── 状态消息 (Markdown)
```

## 事件处理
1. **保存按钮点击**:
   - 获取输入的 API Key
   - 更新 AI 服务凭证
   - 显示操作结果状态

## 使用示例
```python
feedback_service = AIFeedbackService()
settings_tab = SettingsTab(feedback_service)
tab = settings_tab.create()
```

## 安全特性
- API Key 输入框使用密码模式
- 日志中对 API Key 进行脱敏处理
- 使用 HTTPS 进行安全传输

## 用户指南
### API Key 获取步骤
1. 访问 [DeepSeek API](https://platform.deepseek.com/)
2. 注册并登录账号
3. 在控制台中创建 API Key

### 配置说明
- API Key 配置成功后即可使用 AI 分析功能
- 留空 API Key 将禁用 AI 分析功能
- 配置状态会实时显示在界面上

## 注意事项
- API Key 应妥善保管，不要泄露给他人
- 确保输入的 API Key 格式正确
- 配置更改会立即生效
- 使用自定义 CSS 类进行样式控制