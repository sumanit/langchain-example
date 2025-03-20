from langchain_ollama import OllamaEmbeddings

# 初始化模型实例
bge_model = OllamaEmbeddings(
    base_url="http://127.0.0.1:11434",
    model="bge-m3:latest"  # 替换为实际模型名称
)

# 生成文本
response = bge_model.embed_query("请解释人工智能的应用场景。")
print(response)
