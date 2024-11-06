import gradio as gr
import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime

# 加载环境变量
load_dotenv()

# JDoodle API 配置
JDOODLE_CLIENT_ID = os.getenv('JDOODLE_CLIENT_ID')
JDOODLE_CLIENT_SECRET = os.getenv('JDOODLE_CLIENT_SECRET')
JDOODLE_API_URL = "https://api.jdoodle.com/v1/execute"

# 代码示例库
CODE_EXAMPLES = {
    "Hello World": """#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}""",
    "求和计算": """#include <stdio.h>

int main() {
    int a, b;
    printf("请输入两个数字：\\n");
    scanf("%d %d", &a, &b);
    printf("和为：%d\\n", a + b);
    return 0;
}""",
    "九九乘法表": """#include <stdio.h>

int main() {
    for(int i = 1; i <= 9; i++) {
        for(int j = 1; j <= i; j++) {
            printf("%d×%d=%-3d ", j, i, i*j);
        }
        printf("\\n");
    }
    return 0;
}"""
}

def compile_and_run(code, input_data=""):
    """
    使用 JDoodle API 编译和运行 C 代码
    """
    payload = {
        "clientId": JDOODLE_CLIENT_ID,
        "clientSecret": JDOODLE_CLIENT_SECRET,
        "script": code,
        "language": "c",
        "versionIndex": "0",
        "stdin": input_data
    }
    
    try:
        response = requests.post(JDOODLE_API_URL, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            output = result.get('output', '')
            if "error" in output.lower():
                return f"❌ 编译或运行错误:\n{output}"
            return f"✅ 程序输出:\n{output}"
        else:
            return f"❌ API错误: {result.get('error', '未知错误')}"
    except Exception as e:
        return f"❌ 系统错误: {str(e)}"

def load_example(example_name):
    """加载示例代码"""
    return CODE_EXAMPLES.get(example_name, "")

def save_code(code):
    """保存代码到文件"""
    try:
        # 创建保存目录
        os.makedirs("saved_code", exist_ok=True)
        
        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"saved_code/code_{timestamp}.c"
        
        # 保存代码
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        
        return f"✅ 代码已保存到: {filename}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"

# 创建 Gradio 界面
with gr.Blocks(title="EasyC - C语言在线编程学习平台") as demo:
    gr.Markdown("""
    # EasyC - C语言在线编程平台 v0.2
    
    ### 功能说明：
    1. 选择示例代码或编写自己的代码
    2. 如果程序需要输入，请在输入框中提供
    3. 点击运行查看结果
    4. 可以保存代码到本地
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            # 示例选择
            example_dropdown = gr.Dropdown(
                choices=list(CODE_EXAMPLES.keys()),
                label="选择示例代码"
            )
            
            # 代码编辑器
            code_input = gr.Code(
                label="C 代码编辑器",
                language="c",
                value=CODE_EXAMPLES["Hello World"]
            )
            
            # 程序输入
            program_input = gr.Textbox(
                label="程序输入（如果需要）",
                placeholder="多个输入值请用空格分隔",
                lines=2
            )
            
            with gr.Row():
                run_button = gr.Button("运行代码", variant="primary")
                save_button = gr.Button("保存代码")
        
        with gr.Column(scale=1):
            output = gr.Textbox(
                label="程序输出",
                lines=10
            )
    
    # 事件处理
    example_dropdown.change(
        fn=load_example,
        inputs=[example_dropdown],
        outputs=[code_input]
    )
    
    run_button.click(
        fn=compile_and_run,
        inputs=[code_input, program_input],
        outputs=[output]
    )
    
    save_button.click(
        fn=save_code,
        inputs=[code_input],
        outputs=[output]
    )

if __name__ == "__main__":
    demo.launch()