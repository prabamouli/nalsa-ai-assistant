def enforce_guardrails(domain, role):
    if role == "citizen" and domain in ["judicial", "case", "research"]:
        raise PermissionError(
            "This analysis is intended for legal professionals. "
            "For legal assistance, please use the Legal Aid section."
        )
