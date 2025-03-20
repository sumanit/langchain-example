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
pip install langchain langchain_ollama langchain-community
```
# Prompt类继承关系
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
