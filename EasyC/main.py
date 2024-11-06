import gradio as gr
import requests
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# JDoodle API 配置
JDOODLE_CLIENT_ID = os.getenv('JDOODLE_CLIENT_ID')
JDOODLE_CLIENT_SECRET = os.getenv('JDOODLE_CLIENT_SECRET')
JDOODLE_API_URL = "https://api.jdoodle.com/v1/execute"

def compile_and_run(code):
    """
    使用 JDoodle API 编译和运行 C 代码
    """
    payload = {
        "clientId": JDOODLE_CLIENT_ID,
        "clientSecret": JDOODLE_CLIENT_SECRET,
        "script": code,
        "language": "c",
        "versionIndex": "0"
    }
    
    try:
        response = requests.post(JDOODLE_API_URL, json=payload)
        result = response.json()
        
        if response.status_code == 200:
            return result.get('output', '程序输出为空')
        else:
            return f"编译错误: {result.get('error', '未知错误')}"
    except Exception as e:
        return f"系统错误: {str(e)}"

# 创建 Gradio 界面
with gr.Blocks(title="EasyC - C语言在线编程学习平台") as demo:
    gr.Markdown("# EasyC - C语言在线编程平台")
    
    with gr.Row():
        with gr.Column():
            # 使用 Code 组件，它内部使用了 CodeMirror
            code_input = gr.Code(
                label="C 代码编辑器",
                language="c",
                value="""#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}""")
            run_button = gr.Button("运行代码")
        
        with gr.Column():
            output = gr.Textbox(label="程序输出", lines=5)
    
    run_button.click(
        fn=compile_and_run,
        inputs=[code_input],
        outputs=[output]
    )

if __name__ == "__main__":
    demo.launch()