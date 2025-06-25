from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_community.tools.file_management import FileSearchTool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.wikipedia.tool import WikipediaAPIWrapper

# 初始化文件搜索工具（必须设置安全目录）
file_tool = FileSearchTool(root_dir="/Users/suman6/Desktop")  # 替换为实际搜索目录
# 1. 初始化 API 包装器（可配置参数）
api_wrapper = WikipediaAPIWrapper(

    top_k_results=1,            # 返回结果数量
    doc_content_chars_max=200    # 摘要最大字符数
)

# 2. 创建 Wikipedia 查询工具
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
tool_dic = {file_tool.name:file_tool,wikipedia_tool.name:wikipedia_tool}

if __name__ == "__main__":
    # 使用支持工具调用的模型
    ollama_llm = ChatOllama(model="llama3.1:8b", base_url="http://127.0.0.1:11434")

    # 绑定工具
    ollama_llm_with_tools = ollama_llm.bind_tools([file_tool,wikipedia_tool])

    # 使用正确的消息格式
    messages = [HumanMessage(content="what is python")]

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
