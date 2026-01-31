from vector_storage.vectordb import vectorstoredb

user_input = input("Enter your question: ")
retrival = vectorstoredb()
result = retrival.max_marginal_relevance_search(
    query = user_input,
    k=2,
    fetch_k=6,
    lambda_mult=0.6
)

for doc in result:
    print(doc.page_content)