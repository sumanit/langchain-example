from langchain_ollama import OllamaLLM
from common.ollama_helper import get_optimal_deepseek
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate

if __name__ == "__main__":
    model_name = get_optimal_deepseek()
    print(model_name)
    # 初始化模型
    ollama_llm = OllamaLLM(model=model_name,
                           base_url="http://127.0.0.1:11434")  # 默认端口 11434‌:ml-citation{ref="1,5" data="citationList"}

    # 定义子消息模板
    system_msg = SystemMessagePromptTemplate.from_template("你是一个{role}。")
    user_msg = HumanMessagePromptTemplate.from_template("请说一段{theme}的话。")

    # 组合成完整对话模板
    prompt = ChatPromptTemplate.from_messages([system_msg, user_msg])
    print(prompt.format(role="傻逼", theme="傻不拉几"))
    response = (prompt | ollama_llm).invoke({"role": "傻逼", "theme": "傻不拉几"})
    print(response)
