from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate,ChatMessagePromptTemplate

if __name__ == "__main__":
    model_name = get_optimal_deepseek()
    print(model_name)
    # 初始化模型
    ollama_llm = OllamaLLM(model=model_name,
                           base_url="http://127.0.0.1:11434")  # 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

    # 定义子消息模板
    system_msg = SystemMessagePromptTemplate.from_template("你是一个{role}。")
    user_msg = HumanMessagePromptTemplate.from_template("请做一个关于{theme}的五言绝句诗。")
    ai_msg = AIMessagePromptTemplate.from_template("春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。")
    user_msg2 = ChatMessagePromptTemplate.from_template(
        role="user",
        template="还不够 再来一首"  # 使用 theme 变量
    )

    # 组合成完整对话模板
    prompt = ChatPromptTemplate.from_messages([system_msg, user_msg, ai_msg, user_msg2])
    chain = prompt | ollama_llm;
    response =chain.invoke({"role": "唐朝的诗人", "theme": "春天"})
    print(response)
