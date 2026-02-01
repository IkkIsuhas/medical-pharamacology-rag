from rag_app.qa import llm_answer

while True:
    question = input("Ask question(or type exit): ")
    if question.lower() == "exit":
        print("Exiting RAG app")
        break

    answer = llm_answer(question)
    print("Answer: ",answer)