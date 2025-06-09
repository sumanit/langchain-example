from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import FunctionMessage

if __name__ == "__main__":
    # 初始化部分与您原有代码完全一致
    ollama_llm = OllamaLLM(model="deepseek-r1:8b-0528-qwen3-fp16", base_url="http://127.0.0.1:11434")

    # 使用分块消息重构消息模板
    # 定义工具（函数规范）
    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取城市天气数据",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}},
                "required": ["location"]
            }
        }
    }]

    # 创建包含FunctionMessage的对话历史
    messages = [
        ("system", "你是一个有帮助的AI助手"),
        ("human", "查询北京的天气")
    ]

    # 使用ChatPromptTemplate构建提示
    prompt = ChatPromptTemplate.from_messages(messages)

    # 创建链并调用
    chain = prompt | ollama_llm

    response = chain.invoke({},
                            tools=tools,
                            tool_choice="auto"
                            )
    print(response)
    # 解析调用请求并执行函数（示例简化）
    if hasattr(response, "tool_calls"):
        # 实际开发中需调用真实API（如OpenWeatherMap）
        weather_data = {"location": "北京", "temperature": "28℃", "condition": "多云"}
        function_msg = FunctionMessage(name="get_weather", content=str(weather_data))

        # 生成最终回复
        final_response = chain.invoke(
            input=[
                {"role": "user", "content": "北京今天天气怎么样？"},
                function_msg
            ]
        )
        print(final_response.content)

