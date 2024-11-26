# src/frontend/tabs/welcome_tab.py

import gradio as gr

class WelcomeTab:
    def __init__(self):
        pass
        
    def create(self):
        with gr.Tab("EasyC 🚀"):
            # 使用 elem_id 来便于 CSS 定位
            with gr.Column(scale=1, elem_id="welcome-container"):
                gr.Markdown("""
                            # EasyC 🚀 
                            ### 你的专属 C 语言学习伙伴
                            """, elem_id="welcome-header")
                
                gr.Markdown("让编程学习变得轻松有趣，从这里开始你的代码之旅！", 
                          elem_classes=["subtitle"])
                
                # 使用 equal_height=True 使列对齐
                with gr.Row(equal_height=True):
                    with gr.Column(elem_classes=["feature-card"]):
                        gr.Markdown("""
                                    ## 📝 习题练习系统
                                    
                                    ### 为初学者量身打造
                                    - 📚 精心编排的教程与习题
                                    - ⚡ 即时运行与智能评测
                                    - 🤖 AI 助教实时解惑
                                    - 📈 个性化学习进度追踪（即将上线）
                                    """)
                   
                    with gr.Column(elem_classes=["feature-card"]):
                        gr.Markdown("""
                                    ## 🔧 在线编程环境
                                    
                                    ### 专业而简单
                                    - 💻 专业级 C 语言开发环境
                                    - 🚀 零配置，随时随地编程
                                    - 🔍 智能代码提示与纠错
                                    - 🤝 AI 助手伴你编程
                                    """)
                gr.Markdown("> 💡 提示：配置 API Key 后可启用 AI 分析功能，获得更专业的代码建议，让你的学习事半功倍！",
                            elem_classes=["tips"])
