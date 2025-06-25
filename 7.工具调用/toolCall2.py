from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool


@tool
def get_weather(location: str) -> str:
    """Get weather of a location"""
    return "大暴雨"


if __name__ == "__main__":
    # 使用支持工具调用的模型
    ollama_llm = ChatOllama(model="llama3.1:8b", base_url="http://127.0.0.1:11434")

    # 绑定工具
    ollama_llm_with_tools = ollama_llm.bind_tools([get_weather])

    # 使用正确的消息格式
    messages = [HumanMessage(content="杭州天气怎么样?")]

    # 调用模型
    response = ollama_llm_with_tools.invoke(messages)
    print(response.tool_calls)
    # 处理工具调用
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_call = response.tool_calls[0]
        print(tool_call)
        messages.append({"role": "tool", "tool_call_id": tool_call.get("id"), "content":  get_weather.invoke(tool_call['args'])})
        response = ollama_llm_with_tools.invoke(messages)
        print(f"Model Response: {response.content}")
    else:
        print(f"Model Response: {response.content}")