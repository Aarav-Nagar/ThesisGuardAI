# ThesisGuard AI

ThesisGuard AI is a responsible AI investing research assistant that helps users turn vague stock ideas into structured, testable investment theses.

Instead of predicting stock prices or telling users what to buy, ThesisGuard red-teams an investor's thesis using a lightweight analysis pipeline. The goal is to help retail investors avoid hype-driven decisions by forcing every thesis to answer:

- What must go right?
- What could go wrong?
- What evidence supports this?
- What would prove me wrong?
- What should I research before risking money?

## Features

- Single-ticker thesis input and analysis
- Market snapshot retrieval using Yahoo Finance
- Thesis scoring based on specificity, evidence, risk awareness, and valuation awareness
- Markdown research report generation

## Responsible AI Disclaimer

ThesisGuard AI does not provide financial advice, price targets, or buy/sell recommendations. It is a research assistant that helps users structure, challenge, and monitor investment theses.

## Tech Stack

- Streamlit
- Python
- pandas
- yfinance
- plotly

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Example Output

The app generates a report covering:

- cleaned thesis summary
- bull case
- bear case
- thesis breakers
- key metrics to monitor
- an overall thesis health score

## Limitations

- Market data may be delayed or incomplete.
- This tool is for research and education, not financial advice.
- The MVP uses lightweight heuristics rather than a full financial model.
