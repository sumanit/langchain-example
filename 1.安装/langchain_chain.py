from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# 创建 Ollama 实例
llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://127.0.0.1:11434")

# 定义提示模板
prompt = PromptTemplate(
    template="你好"
)

# 创建 LLM 链并运行请求
response = (prompt | llm).invoke({})
print(response)
