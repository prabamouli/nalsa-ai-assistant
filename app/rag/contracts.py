def format_answer(domain, content, sources=None):
    if domain == "nalsa":
        return {
            "answer": content,
            "citations": sources or [],
            "disclaimer": "Information based on NALSA documents."
        }

    if domain == "judicial":
        return {
            "analysis": content,
            "limitations": "Analytical insight, not legal advice."
        }

    if domain == "research":
        return {
            "insights": content,
            "confidence": "Pattern-based"
        }

    return {"response": content}
