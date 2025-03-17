from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
import time
# 初始化模型
ollama_llm = OllamaLLM(model="deepseek-r1:7b", base_url="http://127.0.0.1:11434")  # 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

# 定义提示词模板
prompt = PromptTemplate.from_template("请写一首关于{theme}的诗")
formatted_prompt = prompt.format(theme="春天")
 
set_llm_cache(InMemoryCache())
# 第一次调用
start_time1 = time.time()
# 记录开始时间
response = ollama_llm.invoke(formatted_prompt)
print(response)
elapsed1 = time.time() - start_time1

start_time2 = time.time()
response = ollama_llm.invoke(formatted_prompt)
elapsed2 = time.time() - start_time2
print(response)

print("第一次调用耗时：{:.2f}秒".format(elapsed1))
print("第二次调用耗时：{:.2f}秒".format(elapsed2))