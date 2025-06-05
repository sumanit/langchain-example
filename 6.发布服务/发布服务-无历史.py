from fastapi import FastAPI
from langchain_ollama import OllamaLLM
from langserve import add_routes
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate

from pydantic import BaseModel

class ChatInput(BaseModel):
    question: str
    context: str = None  # 可选字段

model_name = get_optimal_deepseek()
# 初始化模型
ollama_llm = OllamaLLM(model=model_name,
                       base_url="http://127.0.0.1:11434")

# 定义子消息模板
prompt = ChatPromptTemplate.from_template("请用中文回答：{question}")
chain = prompt | ollama_llm  # 历史记录处理器

app = FastAPI(title="小苏",version="V1.0.0",description="基于Langchain的智能助手")
add_routes(app,chain,path="/test")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)