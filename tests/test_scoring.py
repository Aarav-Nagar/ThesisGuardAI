import unittest

from src.scoring.thesis_score import calculate_thesis_score


class ThesisScoringTests(unittest.TestCase):
    def test_specific_thesis_scores_higher(self):
        thesis = (
            "I think NVDA will keep growing because AI data center demand remains strong, "
            "hyperscaler capex continues rising, and margins stay healthy for 12 months."
        )
        market_snapshot = {
            "price": 120.5,
            "one_year_return": 0.45,
            "volatility": 0.03,
            "market_cap": 3.0e12,
            "fifty_two_week_high": 140.0,
            "fifty_two_week_low": 75.0,
        }

        result = calculate_thesis_score(thesis, market_snapshot, "1 year", "Moderate")

        self.assertGreater(result["overall_score"], 50)
        self.assertGreaterEqual(result["specificity_score"], 10)
        self.assertGreaterEqual(result["evidence_score"], 10)
        self.assertGreaterEqual(result["risk_awareness_score"], 8)


if __name__ == "__main__":
    unittest.main()
