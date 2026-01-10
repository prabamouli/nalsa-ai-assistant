from app.rag.llm import call_llm

def retrieve(domain, query):
    prompt = f"""
    Answer the following question strictly as a legal information assistant.
    Question: {query}
    """
    content = call_llm(prompt)

    return {
        "content": content,
        "sources": ["LLM (no documents yet)"]
    }
