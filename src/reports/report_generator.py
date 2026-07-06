def generate_report(ticker: str, thesis: str, horizon: str, risk_tolerance: str, score_result: dict, market_snapshot: dict) -> str:
    """Create a simple markdown report for the thesis analysis."""
    return f"""# ThesisGuard AI Report

- Ticker: {ticker}
- Horizon: {horizon}
- Risk tolerance: {risk_tolerance}
- Thesis health score: {score_result['overall_score']}/100
- Verdict: {score_result['verdict']}

## Your Thesis
{thesis}

## Bull Case
- The thesis identifies a clear market driver.
- The argument highlights demand, capex, or product strength.

## Bear Case
- The thesis could weaken if growth slows or valuation stretches.
- Competitive pressure and margin compression remain key risks.

## Thesis Breakers
- Revenue growth slows materially.
- Gross margin declines sharply.
- Capex commentary turns negative.
- Competitive share gains erode the original view.

## Metrics to Watch
- Price: {market_snapshot.get('price')}
- 1-year return: {market_snapshot.get('one_year_return')}
- Volatility: {market_snapshot.get('volatility')}
- Market cap: {market_snapshot.get('market_cap')}
- 52-week high/low: {market_snapshot.get('fifty_two_week_high')} / {market_snapshot.get('fifty_two_week_low')}

## Score Breakdown
- Specificity: {score_result['specificity_score']}/25
- Evidence: {score_result['evidence_score']}/25
- Risk awareness: {score_result['risk_awareness_score']}/20
- Catalyst clarity: {score_result['catalyst_score']}/15
- Valuation awareness: {score_result['valuation_awareness_score']}/15

## Research Checklist
- Review the latest annual and quarterly filings.
- Compare the thesis against recent earnings and guidance.
- Check whether valuation and sentiment have moved ahead of fundamentals.
- Make note of the evidence that would change your view.
"""
