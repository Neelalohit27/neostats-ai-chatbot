from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


def load_vectorstore():

    docs = [
        Document(page_content="NeoStats is a company focused on AI engineering solutions."),
        Document(page_content="RAG stands for Retrieval Augmented Generation."),
        Document(page_content="LangChain is a framework used to build LLM applications."),
        Document(page_content="Groq provides fast inference for large language models.")
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore