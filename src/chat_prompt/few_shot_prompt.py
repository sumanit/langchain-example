from langchain_ollama import OllamaLLM
from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from common.ollama_helper import get_optimal_deepseek

# 示例数据集（包含复杂查询模式）
examples = [
    {
        "自然语言": "查询2023年华东区销售额过亿的客户",
        "SQL": "SELECT client_name FROM sales WHERE region='华东' AND year=2023 AND total_sales > 100000000;"
    },
    {
        "自然语言": "统计智能手表品类中差评率超过10%的商品",
        "SQL": """\
            SELECT product_id,
                SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)*1.0/COUNT(*) AS bad_rate 
                FROM products 
                WHERE category='智能手表' 
                GROUP BY product_id 
                HAVING bad_rate > 0.1;\
        """
    }
]


def build_sql_prompt():
    example_template = """
        自然语言查询：{自然语言}
        生成SQL：
        ```sql
        {SQL}
        ```
    """

    few_shot_template = FewShotPromptTemplate(
        examples=examples,
        example_prompt=PromptTemplate(
            input_variables=["自然语言", "SQL"],
            template=example_template
        ),
        suffix="自然语言查询：{input}\n生成SQL：\n```sql```\n",
        input_variables=["input"],
        prefix="""\
            你是一个SQL专家，根据示例将自然语言转换为标准SQL：
            数据库结构：
            - sales(client_id, client_name, region, year, total_sales)
            - products(product_id, category, rating, review_count)\
            """
    )
    return HumanMessagePromptTemplate(prompt=few_shot_template)  # 关键修复点


if __name__ == "__main__":
    model_name = get_optimal_deepseek()
    print(f"使用的模型：{model_name}")

    ollama_llm = OllamaLLM(
        model=model_name,
        base_url="http://127.0.0.1:11434"
    )

    # 构建提示流程
    system_msg = SystemMessagePromptTemplate.from_template("你是一个专业的数据库工程师")
    sql_human_msg = build_sql_prompt()

    full_prompt = ChatPromptTemplate.from_messages([
        system_msg,
        sql_human_msg
    ])

    # 执行查询
    chain = full_prompt | ollama_llm
    response = chain.invoke({
        "input": "找出2024年Q2购买过VR设备但未买游戏主机的客户"
    })

    print("\n生成的SQL：")
    print(response)
