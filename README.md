# 环境安装
1. 创建lagnchain的项目环境  
```
python3 -m venv langchain
```
2.  激活环境
```
source langchain/bin/activate
```
3. 更新pip
```
pip install --upgrade pip
```
4. 安装langchain
```
pip install langchain langchain_core langchain_ollama langchain-community
```
# Message类继承关系
模型需要的是消息列表。因此，可以通过 `MessagePromptTemplate` 生成单个结构化消息（`Message` 对象），再通过 `PromptTemplate` 将这些消息组织成对话列表。

Message 不支持占位符 一般不会直接构建  会通过MessagePromptTemplate构建得到

```
BaseMessage 基类
 +-- SystemMessage 系统消息
 +-- HumanMessage 用户消息
 +-- AIMessage 模型回复消息
 +-- ChatMessage 通用消息
 +-- FunctionMessage  
 +-- ToolMessage
 +-- BaseMessageChunk
      +-- SystemMessageChunk
      +-- AIMessageChunk
      +-- HumanMessageChunk
      +-- ChatMessageChunk
      +-- FunctionMessageChunk
      +-- ToolMessageChunk
```
MessagePromptTemplate 用于通过模板生成各种类型的Message 
```
BaseMessagePromptTemplate 基类
 +-- _StringImageMessagePromptTemplate 
      +-- AIMessagePromptTemplate
      +-- HumanMessagePromptTemplate
      +-- SystemMessagePromptTemplate
 +-- BaseStringMessagePromptTemplate
      +-- ChatMessagePromptTemplate
 +-- MessagesPlaceholder    
```

PromptTemplate 用于通过模板生成调用模型的Message列表 
```
BasePromptTemplate
 +-- BaseChatPromptTemplate
      +-- ChatPromptTemplate
      |    +-- StructuredPrompt
      |    +-- AgentScratchPadChatPromptTemplate  
      +-- FewShotChatMessagePromptTemplate
 +-- StringPromptTemplate
      +-- PromptTemplate 
      +-- FewShotPromptTemplate
      +-- FewShotPromptWithTemplates
 +-- PipelinePromptTemplate
 +-- ImagePromptTemplate
```

# Selector
用于在PromptTemplate中进行示例的选择 根据用户的输入 筛选合适的示例提供给大模型

```
BaseExampleSelector
 +-- LengthBasedExampleSelector
 +-- MaxMarginalRelevanceExampleSelector
 +-- _VectorStoreExampleSelector
    +-- MaxMarginalRelevanceExampleSelector
    +-- SemanticSimilarityExampleSelector
 +-- NGramOverlapExampleSelector
```

