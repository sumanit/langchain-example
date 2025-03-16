"""
# 创建lagnchain的项目环境
python3 -m venv langchain
# 激活环境
source langchain/bin/activate
# 更新pip
pip install --upgrade pip
# 安装langchain
pip install langchain
# 安装 langchain_ollama
pip install langchain_ollama
"""

from langchain_ollama import OllamaLLM
from src.common.ollama_helper import get_optimal_deepseek
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

if __name__ == "__main__":
    model_name=get_optimal_deepseek()
    print(model_name)
    # 初始化模型
    ollama_llm = OllamaLLM(model=model_name, base_url="http://127.0.0.1:11434")# 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

    # 定义提示词模板
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(
            content="You are a helpful assistant! Your name is Bob."
        ),
        HumanMessage(
            content="{user_input} What is your name?"
        )
    ])
    user_input = {"user_input": "你好"}
    response = (prompt | ollama_llm).invoke(user_input)
    print(response)