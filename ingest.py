from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

def ingest():
    docs = []

    # Load PDFs
    print("Loading PDFs...")
    for filename in os.listdir("data/"):
        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(f"data/{filename}")
            docs.extend(loader.load())

    # Load .txt files
    print("Loading text files...")
    for filename in os.listdir("data/"):
        if filename.endswith(".txt"):
            loader = TextLoader(f"data/{filename}")
            docs.extend(loader.load())

    # Load .md files
    print("Loading markdown files...")
    for filename in os.listdir("data/"):
        if filename.endswith(".md"):
            loader = TextLoader(f"data/{filename}")
            docs.extend(loader.load())

    print(f"Loaded {len(docs)} total documents")

    # Split into chunks
    print("Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # Embed and store
    print("Embedding and storing in ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )
    print("Done. Vectorstore saved to chroma_db/")

if __name__ == "__main__":
    ingest()
