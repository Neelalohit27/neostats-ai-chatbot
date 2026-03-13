from langchain_community.tools import DuckDuckGoSearchRun

def web_search(query: str):
    """
    Perform live web search.
    """
    search = DuckDuckGoSearchRun()
    result = search.run(query)
    return result