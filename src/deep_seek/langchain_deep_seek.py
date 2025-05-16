from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain.prompts import PromptTemplate

model_name=get_optimal_deepseek()
print(model_name)
# 初始化模型
ollama_llm = OllamaLLM(model=model_name, base_url="http://127.0.0.1:11434")# 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

# 定义提示词模板
prompt = PromptTemplate.from_template("请写一首关于{theme}的诗")
formatted_prompt = prompt.format(theme="春天")

stream = True
# 调用模型生成内容 一次返回
if(stream): 
    ## 流式返回
    for chunk in ollama_llm.stream(formatted_prompt, raw=True):
        print(type(chunk))
        print(chunk)
else:
    response = ollama_llm.invoke(formatted_prompt)
