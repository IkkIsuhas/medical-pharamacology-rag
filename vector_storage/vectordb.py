from langchain_community.vectorstores import FAISS
from injection.embedding import embedding_model
from injection.splitter import docs_splitter

def vectorstoredb():
    print("Process started: Loading and splitting documents...")
    chunk = docs_splitter()
    print(f"Documents split into {len(chunk)} chunks.")
    
    print("Initializing embedding model (this may take a moment)...")
    model = embedding_model()
    
    print("Creating FAISS vector store...")
    storedb = FAISS.from_documents(chunk, model)
    return storedb
print("Embedding stored successfully!!")