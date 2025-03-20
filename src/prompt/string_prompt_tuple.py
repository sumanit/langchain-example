from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import PromptTemplate

if __name__ == "__main__":
    model_name = get_optimal_deepseek()
    print(model_name)
    # 初始化模型
    ollama_llm = OllamaLLM(model=model_name,
                           base_url="http://127.0.0.1:11434")  # 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

    # 定义提示词模板
    prompt = PromptTemplate.from_template("{user_input}")
    user_input = {"user_input": "你好"}
    print(prompt)
    response = (prompt | ollama_llm).invoke(user_input)
    print(response)
