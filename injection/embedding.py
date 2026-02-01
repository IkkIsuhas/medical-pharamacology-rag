from langchain_community.embeddings import HuggingFaceBgeEmbeddings
#Qwen/Qwen3-Embedding-0.6B
def embedding_model():
    model = HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return model
print("Embedding model initialized successfully")