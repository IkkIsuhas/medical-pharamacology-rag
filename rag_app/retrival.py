from vector_storage.load_vector import load_vectorstore

def retriever_chunk(question :str):
    retrival = load_vectorstore()
    result = retrival.similarity_search(
        query = question,
        k=2
    )
    chunks = []
    for doc in result:
        chunks.append(doc.page_content)

    return chunks