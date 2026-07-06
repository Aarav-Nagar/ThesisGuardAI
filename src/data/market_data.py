import yfinance as yf


def fetch_market_data(ticker: str) -> dict:
    """Return a lightweight market snapshot for a ticker."""
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2y")
        info = stock.info

        if hist.empty:
            return {
                "ticker": ticker,
                "price": None,
                "one_year_return": None,
                "volatility": None,
                "market_cap": None,
                "fifty_two_week_high": None,
                "fifty_two_week_low": None,
                "error": "No price history available",
            }

        latest_close = float(hist["Close"].iloc[-1])
        prev_close = float(hist["Close"].iloc[-252]) if len(hist) >= 252 else float(hist["Close"].iloc[0])
        one_year_return = (latest_close / prev_close - 1.0) * 100.0 if prev_close else None
        returns = hist["Close"].pct_change().dropna()
        volatility = float(returns.std() * (252**0.5)) if not returns.empty else None

        return {
            "ticker": ticker,
            "price": latest_close,
            "one_year_return": one_year_return,
            "volatility": volatility,
            "market_cap": info.get("marketCap"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            "error": None,
        }
    except Exception as exc:
        return {
            "ticker": ticker,
            "price": None,
            "one_year_return": None,
            "volatility": None,
            "market_cap": None,
            "fifty_two_week_high": None,
            "fifty_two_week_low": None,
            "error": str(exc),
        }
