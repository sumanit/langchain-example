from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 创建 Ollama 实例
llm = OllamaLLM(model="deepseek-r1:14b", base_url="http://127.0.0.1:11434")

# 定义提示模板
prompt = PromptTemplate(
    input_variables=["question"],
    template="请回答以下问题: {question}"
)

# 创建 LLM 链并运行请求
response = (prompt | llm).invoke("你好")
print(response)