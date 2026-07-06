def build_evidence_check(thesis: str) -> list[str]:
    """Return evidence questions that should be answered before acting on the thesis."""
    return [
        "What revenue, margin, or valuation evidence supports the thesis?",
        "How would you know the thesis is wrong?",
    ]
