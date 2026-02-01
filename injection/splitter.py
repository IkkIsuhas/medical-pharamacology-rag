from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from .loader import doc_loader

def docs_splitter():
    docs = doc_loader()
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
    chunk = splitter.split_documents(docs)
    return chunk
print("Document has been converted into chunks successfully!!")
