from langchain_community.vectorstores import FAISS
from injection.embedding import embedding_model

def load_vectorstore():
    model = embedding_model()
    return FAISS.load_local("faiss_index", model)
