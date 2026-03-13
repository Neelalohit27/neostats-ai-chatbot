from utils.web_search import web_search

def retrieve_context(question, vectorstore):

    docs = vectorstore.similarity_search(question)

    if len(docs) == 0:
        # fallback to live web search
        return web_search(question)

    context = "\n".join([doc.page_content for doc in docs])

    return context