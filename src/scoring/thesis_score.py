import re


def calculate_thesis_score(thesis: str, market_snapshot: dict, horizon: str, risk_tolerance: str) -> dict:
    """Create a simple heuristic-based thesis health score."""
    text = thesis.lower()

    specificity_score = 10
    if len(text.split()) >= 20:
        specificity_score += 5
    if re.search(r"\b(revenue|margin|valuation|growth|capex|demand|competitive|cash|earnings)\b", text):
        specificity_score += 8
    if re.search(r"\b(12 months|1 year|3 years|quarter|quarterly|next|during)\b", text):
        specificity_score += 4
    specificity_score = min(specificity_score, 25)

    evidence_score = 8
    if re.search(r"\b(revenue|margin|valuation|growth|capex|demand|cash|earnings|multiple)\b", text):
        evidence_score += 10
    if re.search(r"\b(number|percent|million|billion|price|multiple|ratio)\b", text):
        evidence_score += 7
    evidence_score = min(evidence_score, 25)

    risk_awareness_score = 10
    if re.search(r"\b(risk|downside|valuation|competition|bear|weak|slow|regulation|supply)\b", text):
        risk_awareness_score += 6
    if risk_tolerance.lower() == "conservative":
        risk_awareness_score += 2
    risk_awareness_score = min(risk_awareness_score, 20)

    catalyst_score = 8
    if horizon.lower() in {"1 year", "3 years"}:
        catalyst_score += 4
    if market_snapshot.get("price"):
        catalyst_score += 3
    catalyst_score = min(catalyst_score, 15)

    valuation_awareness_score = 6
    if market_snapshot.get("price") and market_snapshot.get("fifty_two_week_high"):
        valuation_awareness_score += 4
    if market_snapshot.get("one_year_return") is not None:
        valuation_awareness_score += 3
    valuation_awareness_score = min(valuation_awareness_score, 15)

    overall_score = specificity_score + evidence_score + risk_awareness_score + catalyst_score + valuation_awareness_score

    if overall_score >= 80:
        verdict = "Strong"
    elif overall_score >= 60:
        verdict = "Needs Research"
    elif overall_score >= 40:
        verdict = "Weak"
    else:
        verdict = "Speculative"

    return {
        "specificity_score": specificity_score,
        "evidence_score": evidence_score,
        "risk_awareness_score": risk_awareness_score,
        "catalyst_score": catalyst_score,
        "valuation_awareness_score": valuation_awareness_score,
        "overall_score": overall_score,
        "verdict": verdict,
    }
