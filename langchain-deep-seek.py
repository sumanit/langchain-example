from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# 初始化模型
ollama_llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://localhost:11434")  # 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

# 定义提示词模板
prompt = PromptTemplate.from_template("请写一首关于{theme}的诗")
formatted_prompt = prompt.format(theme="春天")

stream = True
# 调用模型生成内容 一次返回
if(stream): 
    ## 流式返回
    for chunk in ollama_llm.stream(formatted_prompt):
        print(chunk)
else:
    response = ollama_llm.invoke(formatted_prompt)
