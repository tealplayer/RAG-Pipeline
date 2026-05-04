import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    return vectorstore

def retrieve(vectorstore, query, k=5):
    results = vectorstore.similarity_search(query, k=k)
    print("\n--- Retrieved Chunks ---")
    for i, r in enumerate(results):
        print(f"\nChunk {i+1}:\n{r.page_content}")
    print("------------------------\n")
    return "\n\n".join([r.page_content for r in results])

def answer(llm, query, context):
    prompt = ChatPromptTemplate.from_template("""
You are a clinical trial research assistant.
Answer the question using only the context provided from research papers.
If the context doesn't contain enough information, say so.

Context:
{context}

Question: {query}
""")
    chain = prompt | llm
    response = chain.invoke({"context": context, "query": query})
    return response.content

if __name__ == "__main__":
    vectorstore = load_vectorstore()
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.environ["GROQ_API_KEY"]
    )

    while True:
        query = input("\nAsk a question (or 'quit'): ")
        if query.lower() == "quit":
            break

        context = retrieve(vectorstore, query)
        response = answer(llm, query, context)
        print(f"\n{response}")
