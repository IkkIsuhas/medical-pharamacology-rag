from langchain_community.document_loaders import PDFPlumberLoader

def doc_loader():
    loader = PDFPlumberLoader("data/medical_pharmacology.pdf")
    docs = loader.load()
    return docs

print("Document loaded successfully!!")