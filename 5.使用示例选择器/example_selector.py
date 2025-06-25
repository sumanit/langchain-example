from langchain_ollama import OllamaLLM
from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.example_selectors.semantic_similarity import SemanticSimilarityExampleSelector
from common.ollama_helper import get_optimal_deepseek
from langchain_community.vectorstores import  Chroma
from langchain_ollama import OllamaEmbeddings

# 示例数据集（包含复杂查询模式）
examples = [
    {
        "input": "我想买一些可以治疗头疼的药",
        "intent": "买药"
    },
    {
        "input": "我头特别疼已经很久了",
        "intent": "问诊"
    },
    {
        "input": "我现在就需要买一些感冒药",
        "intent": "线下买药"
    },
    {
        "input": "布洛芬吃的时候需要注意什么",
        "intent": "用药咨询"
    },
    {
        "input": "体重有点超标了应该怎么处理",
        "intent": "健康管理"
    }
]


def build_human_prompt():
    example_template = """用户输入：{input}
                          用户意图：{intent}"""
    # 初始化模型实例
    bge_model = OllamaEmbeddings(
        base_url="http://127.0.0.1:11434",
        model="bge-m3:latest"  # 替换为实际模型名称
    )
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        bge_model,
        Chroma,
        k=1
    )

    few_shot_template = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=PromptTemplate(
            input_variables=["input", "intent"],
            template=example_template
        ),
        suffix="用户输入：{input}\n判断用户意图：\n```intent```\n",
        input_variables=["input"],
        prefix="""\
            你是一个健康咨询专家，根据示例将判断用户意图：\
            """
    )
    return HumanMessagePromptTemplate(prompt=few_shot_template)


if __name__ == "__main__":
    model_name = get_optimal_deepseek()
    print(f"使用的模型：{model_name}")

    ollama_llm = OllamaLLM(
        model=model_name,
        base_url="http://127.0.0.1:11434"
    )

    # 构建提示流程
    system_msg = SystemMessagePromptTemplate.from_template("你是一个专业的健康咨询师")
    sql_human_msg = build_human_prompt()

    full_prompt = ChatPromptTemplate.from_messages([
        system_msg,
        sql_human_msg
    ])
    print(full_prompt.invoke({
        "input": "我的牙很疼"
    }))
    # 执行查询
    chain = full_prompt | ollama_llm
    response = chain.invoke({
        "input": "我的牙很疼"
    })

    print("\n用户意图：")
    print(response)
