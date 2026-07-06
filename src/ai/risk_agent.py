def build_risk_review(risk_tolerance: str) -> list[str]:
    """Return a simple risk review based on the chosen risk profile."""
    return [
        f"Risk tolerance selected: {risk_tolerance}.",
        "Position sizing and downside planning should be considered before acting.",
    ]
