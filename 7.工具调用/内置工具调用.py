from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_community.tools.file_management import FileSearchTool
from langchain_community.tools.wikipedia.tool import (
        WikipediaQueryRun,WikipediaAPIWrapper
    )

# 初始化文件搜索工具（必须设置安全目录）
file_tool = FileSearchTool(root_dir="/Users/suman6/Desktop")  # 替换为实际搜索目录
wikipedia_api_wrapper = WikipediaAPIWrapper()
wikipedia_query_run = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)
tools = [file_tool,wikipedia_query_run]
tool_dic = {item.name: item for item in tools}
if __name__ == "__main__":
    # 使用支持工具调用的模型
    ollama_llm = ChatOllama(model="llama3.1:8b", base_url="http://127.0.0.1:11434")

    # 绑定工具
    ollama_llm_with_tools = ollama_llm.bind_tools(tools)

    # 使用正确的消息格式
    messages = [HumanMessage(content="what is card")]

    # 调用模型
    response = ollama_llm_with_tools.invoke(messages)
    print(response.tool_calls)
    # 处理工具调用
    if hasattr(response, 'tool_calls') and response.tool_calls:
        tool_call = response.tool_calls[0]
        print(f"触发工具调用: {tool_call['name']},{tool_call['args']}")
        tool = tool_dic.get(tool_call['name'])
        # 执行工具并更新消息历史
        args = tool_call['args']
        tool_result = tool.invoke(args)
        print(tool_result)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.get("id"),
            "content": str(tool_result)  # 确保转换为字符串
        })

        # 获取最终响应
        final_response = ollama_llm_with_tools.invoke(messages)
        print(f"最终结果: {final_response.content}")
    else:
        print(f"直接响应: {response.content}")
