from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def embedding_model():
    model = HuggingFaceBgeEmbeddings(
        model_name="Qwen/Qwen3-Embedding-0.6B",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return model
print("Embedding model initialized successfully")