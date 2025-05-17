from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage, ChatMessage


if __name__ == "__main__":
    # 初始化部分与您原有代码完全一致
    model_name = get_optimal_deepseek()
    ollama_llm = OllamaLLM(model=model_name, base_url="http://127.0.0.1:11434")

    # 使用分块消息重构消息模板
    system_message = SystemMessage("你是一唐朝的诗人。")
    human_message = HumanMessage("请做一个关于春天的五言绝句诗。")
    ai_message = AIMessage("春眠不觉晓，处处闻啼鸟。")  # 初始AI响应分块
    follow_up_message = ChatMessage("还不够 再来一首",role="human")

    # 格式化成完整提示（保持与您原有输出格式一致）
    formatted_prompt = ChatPromptTemplate.from_messages( [
        system_message,
        human_message,
        ai_message,
        follow_up_message
    ])


    # 打印下处理好的消息
    print(formatted_prompt.invoke({}))

    chain = formatted_prompt|ollama_llm
    response = chain.invoke({},stream=True)
    print(response)
