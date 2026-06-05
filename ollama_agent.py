import os

import numexpr

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return vectorstore

@tool
def search_documents(query: str) -> str:
    '''Search the clinical trial research documents and reddit posts for revelant information.'''
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = Chroma(
        persist_directory='chroma_db',
        embedding_function=embeddings
    )
    results = vectorstore.similarity_search(query, k=5)

    return "\n\n".join([r.page_content for r in results])

@tool
def calculate(expression: str) -> str:
    '''Evaluate a mathematical expression. Input should be a valid math expression like '2 * (3 + 4)' or 'sqrt(64)'.'''
    try:
        result = numexpr.evaluate(expression).item()
        return str(result)
    
    except Exception as e:
        return f"Error evaluating expression: {e}"
    
def build_agent(llm, tools):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a clinical trial research assistant. 
         
    Use the search_documents tool to find relevant information from research papers.
    Use the calculate tool when you need to do math.
        
        Always ground your answers in the retrieved documents."""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name='agent_scratchpad')
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    store = {}
    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        
        return store[session_id]
    
    return RunnableWithMessageHistory(
        executor,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history"
    )

if __name__ == "__main__":
    llm = ChatOllama(
        model='llama3.1:8b',
        temperature=0.1
    )
    tools = [search_documents, calculate]
    agent_executor = build_agent(llm, tools)

    while True:
        query = input("\nAsk a question (or 'quit'): ")
        if query.lower().strip() == "quit":
            break

        response = agent_executor.invoke({"input": query}, config={"configurable": {"session_id": "main"}})
        print(f"\n{response['output']}")
