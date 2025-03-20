from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

if __name__ == "__main__":
    # 初始化部分与您原有代码完全一致
    model_name = get_optimal_deepseek()
    ollama_llm = OllamaLLM(model=model_name, base_url="http://127.0.0.1:11434")

    # 使用分块消息重构消息模板
    system_chunk =SystemMessage("你是一唐朝的诗人。")
    human_chunk = HumanMessage("请做一个关于春天的五言绝句诗。")
    ai_chunk = AIMessage("春眠不觉晓，处处闻啼鸟。")  # 初始AI响应分块
    follow_up_chunk = HumanMessage("还不够 再来一首")

    # 构建分块消息序列（模拟流式响应）
    message_sequence = [
        system_chunk,
        human_chunk,
        ai_chunk,
        follow_up_chunk
    ]

    # 格式化成完整提示（保持与您原有输出格式一致）
    formatted_prompt = ChatPromptTemplate.from_messages(message_sequence)


    # 实际调用时的分块处理（需要模型支持流式）
    print(formatted_prompt.invoke({}))
    response = (formatted_prompt|ollama_llm).invoke({})

    print(response)
