from langchain_openai import ChatOpenAI
from langchain_classic.schema import SystemMessage, HumanMessage
from .retrival import retriever_chunk
from dotenv import load_dotenv
import os
load_dotenv()

def llm_answer(question:str):
    model = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="deepseek/deepseek-r1-0528:free",
        temperature=0.2
    )

    context = "\n\n".join(retriever_chunk(question))
    system_message = SystemMessage(
        content=(
            "You are a helpful assistant.\n"
            "Answer ONLY using the context below.\n"
            "If the answer is not in the context, say 'I don't know'."
        )
    )

    human_message = HumanMessage(
        f"Context: {context}\n\n Question: {question}"
        )
    response = model.invoke([system_message, human_message])
    return response.content