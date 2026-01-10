from app.rag.domains import Domain

def route_query(query: str) -> Domain:
    q = query.lower()

    if any(x in q for x in ["free legal aid", "nalsa", "lok adalat", "eligibility"]):
        return Domain.NALSA

    if any(x in q for x in ["judge", "appeal", "wrong judgment", "constitutional"]):
        return Domain.JUDICIAL

    if any(x in q for x in ["draft", "petition", "grounds", "mindmap"]):
        return Domain.CASE

    if any(x in q for x in ["trend", "statistics", "pattern", "over years"]):
        return Domain.RESEARCH

    # default safe fallback
    return Domain.NALSA
