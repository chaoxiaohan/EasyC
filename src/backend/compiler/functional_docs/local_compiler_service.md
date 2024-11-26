# LocalCompilerService 类文档

## 文件位置
`src/backend/compiler/local_compiler_service.py`

## 功能概述
`LocalCompilerService` 是一个本地编译和运行代码的服务类，负责接收代码并在本地环境中编译和执行。该类专注于代码的编译和执行功能。

## 类结构
### 主要依赖
- `os`: 用于文件和目录操作
- `subprocess`: 用于执行外部命令
- `uuid`: 用于生成唯一文件名
- `typing`: 提供类型提示
- `utils.logger`: 提供日志记录功能

### 构造函数
```python
def __init__(self):
```
- 功能:
    - 初始化编译目录 `/tmp/compile`
    - 创建编译目录并记录初始化日志

### 主要方法
**compile_and_run**
```python
async def compile_and_run(self, code: str, input_data: Optional[str] = None) -> Dict:
```
- 参数:
    - `code`: 需要编译和运行的代码
    - `input_data`: 可选的输入数据
- 功能:
    - 编译并运行代码
    - 使用 GCC 编译器，启用安全编译选项
    - 设置 5 秒超时限制
    - 自动清理临时文件
- 返回值: 包含以下字段的字典
    - `success`: 布尔值，表示是否成功
    - `output`: 格式化的输出信息
    - `error`: 错误信息（如果有）
    - `execution_time`: 执行时间（本地运行固定为 0.0）
- 异常处理:
    - 编译错误
    - 运行时错误
    - 超时错误
    - 其他异常

### 工作流程
1. 初始化时创建编译目录
2. 接收代码并生成唯一的临时文件
3. 使用 GCC 编译代码（启用安全选项）
4. 执行编译后的程序
5. 返回执行结果
6. 清理临时文件

### 安全特性
- 使用 `-Wall` 启用所有警告
- 使用 `-fstack-protector-strong` 增强栈保护
- 使用 `-D_FORTIFY_SOURCE=2` 启用运行时缓冲区检查
- 使用 `-O2` 优化级别
- 5秒执行超时限制

### 使用示例
```python
# 初始化服务
compiler_service = LocalCompilerService()

# 编译并运行代码
code = '''
#include <stdio.h>
int main() {
    printf("Hello, World!\\n");
    return 0;
}
'''
result = await compiler_service.compile_and_run(code)
print(result['output'])
```

### 返回值示例
成功情况：
```python
{
    "success": True,
    "output": "✅ 运行成功！程序输出:\n---\nHello, World!",
    "error": "",
    "execution_time": 0.0
}
```

错误情况：
```python
{
    "success": False,
    "output": "❌ 编译错误:\n---\n[错误详情]",
    "error": "[错误详情]",
    "execution_time": 0.0
}
```