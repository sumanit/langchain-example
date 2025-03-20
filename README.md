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
# Prompt类继承关系
模型需要的是消息列表。因此，可以通过 `MessagePromptTemplate` 生成单个结构化消息（`Message` 对象），再通过 `ChatPromptTemplate` 将这些消息组织成对话列表。
- Message 不支持占位符
```
BaseMessage
 +-- SystemMessage
 +-- HumanMessage
 +-- AIMessage
 +-- ChatMessage
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

```
BaseMessagePromptTemplate
 +-- _StringImageMessagePromptTemplate
      +-- AIMessagePromptTemplate
      +-- HumanMessagePromptTemplate
      +-- SystemMessagePromptTemplate
 +-- BaseStringMessagePromptTemplate
      +-- ChatMessagePromptTemplate
 +-- MessagesPlaceholder    
```

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

```
BaseExampleSelector
 +-- LengthBasedExampleSelector
 +-- MaxMarginalRelevanceExampleSelector
 +-- _VectorStoreExampleSelector
    +-- MaxMarginalRelevanceExampleSelector
    +-- SemanticSimilarityExampleSelector
 +-- NGramOverlapExampleSelector
```

