from fastapi import FastAPI
from langchain_community.chat_message_histories import FileChatMessageHistory, SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, MarkdownListOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_ollama import OllamaLLM
from langserve import add_routes
from pydantic import ConfigDict
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

model_name = get_optimal_deepseek()
print(model_name)
# 初始化模型
ollama_llm = OllamaLLM(model=model_name,
                       base_url="http://127.0.0.1:11434")

# 定义子消息模板
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是健康智能助手."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)
chain = prompt | ollama_llm | StrOutputParser() # 历史记录处理器
def get_message_history(session_id: str) -> FileChatMessageHistory:
    print(session_id)
    return FileChatMessageHistory(file_path=f"./history/{session_id}.json")
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_message_history,
    input_messages_key="question",
    history_messages_key="history",
)

app = FastAPI(title="小苏",version="V1.0.0",description="基于Langchain的智能助手")
add_routes(app,chain_with_history,path="/chatTest")
ConfigDict(arbitrary_types_allowed=True)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)