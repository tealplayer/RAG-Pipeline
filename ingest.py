from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def ingest():
    # 1. Load all PDFs
    print("Loading PDFs...")
    loader = PyPDFDirectoryLoader("data/")
    docs = loader.load()
    print(f"Loaded {len(docs)} pages")

    # 2. Split into chunks
    print("Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # 3. Embed and store
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

