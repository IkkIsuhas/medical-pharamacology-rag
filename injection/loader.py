from langchain_community.document_loaders import UnstructuredPDFLoader

def doc_loader():
    loader = UnstructuredPDFLoader("data/medical_pharmacology.pdf")
    docs = loader.load()
    return docs

print("Document loaded successfully!!")