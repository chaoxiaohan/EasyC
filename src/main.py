import os
import sys

# 配置工作目录
sys.path.append(os.path.dirname(os.path.abspath("main")))

import gradio as gr
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from examples.code_examples import CODE_EXAMPLES
import sqlite3
import pandas as pd



# 加载环境变量
load_dotenv()

# JDoodle API 配置
JDOODLE_CLIENT_ID = os.getenv('JDOODLE_CLIENT_ID')
JDOODLE_CLIENT_SECRET = os.getenv('JDOODLE_CLIENT_SECRET')
JDOODLE_API_URL = "https://api.jdoodle.com/v1/execute"

# 初始化数据库
def init_db():
    conn = sqlite3.connect('code_history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  code TEXT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                  result TEXT)''')
    conn.commit()
    conn.close()

init_db()

def save_to_history(code, result):
    """保存代码到历史记录"""
    conn = sqlite3.connect('code_history.db')
    c = conn.cursor()
    c.execute("INSERT INTO history (code, result) VALUES (?, ?)", (code, result))
    conn.commit()
    conn.close()

def get_history():
    """获取历史记录"""
    conn = sqlite3.connect('code_history.db')
    history = pd.read_sql_query("SELECT * FROM history ORDER BY timestamp DESC LIMIT 10", conn)
    conn.close()
    return history

def compile_and_run(code, input_data=""):
    """使用 JDoodle API 编译和运行 C 代码"""
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
            result_text = f"✅ 程序输出:\n{output}" if "error" not in output.lower() else f"❌ 编译或运行错误:\n{output}"
            # 保存到历史记录
            save_to_history(code, result_text)
            return result_text
        else:
            error_text = f"❌ API错误: {result.get('error', '未知错误')}"
            save_to_history(code, error_text)
            return error_text
    except Exception as e:
        error_text = f"❌ 系统错误: {str(e)}"
        save_to_history(code, error_text)
        return error_text

def load_example(category, example_name):
    """加载示例代码"""
    if category and example_name:
        return CODE_EXAMPLES[category][example_name]["code"], CODE_EXAMPLES[category][example_name]["description"]
    return "", ""

def save_code_to_file(code, file_name):
    """保存代码到文件"""
    try:
        os.makedirs("saved_code", exist_ok=True)
        file_path = os.path.join("saved_code", file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        return f"✅ 代码已保存到: {file_path}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"

def load_code_from_file(file_obj):
    """从文件加载代码"""
    try:
        content = file_obj.decode('utf-8')
        return content
    except Exception as e:
        return f"❌ 文件加载失败: {str(e)}"

# 创建 Gradio 界面
with gr.Blocks(title="EasyC - C语言在线编程学习平台") as demo:
    gr.Markdown("""
    # EasyC - C语言在线编程平台 v0.3
    
    ### 新功能：
    1. 代码历史记录
    2. 文件上传下载
    3. 更多示例代码
    4. 分类示例浏览
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            # 示例选择
            with gr.Row():
                category_dropdown = gr.Dropdown(
                    choices=list(CODE_EXAMPLES.keys()),
                    label="选择类别"
                )
                example_dropdown = gr.Dropdown(
                    label="选择示例"
                )
            
            example_description = gr.Textbox(
                label="示例说明",
                interactive=False
            )
            
            # 代码编辑器
            code_input = gr.Code(
                label="C 代码编辑器",
                language="c",
                value=CODE_EXAMPLES["基础示例"]["Hello World"]["code"]
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
                
            # 文件上传下载
            with gr.Row():
                file_upload = gr.File(label="上传代码文件")
                file_download = gr.Textbox(label="保存文件名", placeholder="example.c")
        
        with gr.Column(scale=1):
            output = gr.Textbox(
                label="程序输出",
                lines=10
            )
            
            # 历史记录
            history_df = gr.DataFrame(
                label="代码历史记录",
                headers=["ID", "代码", "时间", "结果"],
                interactive=False
            )
    
    # 事件处理
    def update_examples(category):
        if category:
            return gr.Dropdown(choices=list(CODE_EXAMPLES[category].keys()))
        return gr.Dropdown(choices=[])
    
    category_dropdown.change(
        fn=update_examples,
        inputs=[category_dropdown],
        outputs=[example_dropdown]
    )
    
    example_dropdown.change(
        fn=load_example,
        inputs=[category_dropdown, example_dropdown],
        outputs=[code_input, example_description]
    )
    
    run_button.click(
        fn=compile_and_run,
        inputs=[code_input, program_input],
        outputs=[output]
    ).then(
        fn=get_history,
        outputs=[history_df]
    )
    
    save_button.click(
        fn=save_code_to_file,
        inputs=[code_input, file_download],
        outputs=[output]
    )
    
    file_upload.change(
        fn=load_code_from_file,
        inputs=[file_upload],
        outputs=[code_input]
    )

if __name__ == "__main__":
    demo.launch()