# Costco FY2025 10-K: DRIVER DCF review

Costco Wholesale Corporation's latest Form 10-K covers the fiscal year ended **August 31, 2025**. Dollar amounts are in millions unless stated otherwise.

## D — Disclosure and source discipline

The financial-statement inputs below are from Costco's FY2025 Form 10-K. Forecasts and market-based assumptions are labeled rather than presented as reported facts. The market price is outside the 10-K and is separately identified.

## R — Research: sourced financial inputs

| Input | Value | Source and calculation |
|---|---:|---|
| Operating cash flow | $13,335 | Consolidated Statements of Cash Flows, FY2025 |
| Additions to property and equipment | $5,498 | Consolidated Statements of Cash Flows, FY2025 |
| Interest expense | $154 | Item 7, FY2025 |
| Effective tax rate | 25.1% | Item 7, FY2025 |
| Starting FCFF | $7,952.3 | $13,335 + [$154 x (1 - 25.1%)] - $5,498 |
| Net sales: FY2025 / FY2024 / FY2023 | $269,912 / $249,625 / $237,710 | Item 7, Net Sales |
| FY2023-FY2025 net-sales CAGR | 6.5583% | ($269,912 / $237,710)^(1/2) - 1 |
| Cash and cash equivalents | $14,161 | Consolidated Balance Sheets, August 31, 2025 |
| Total long-term debt | $5,805 | Note 4, Long-Term Debt, August 31, 2025 |
| Weighted-average diluted shares | 444.803 million | Note 9, Net Income per Common and Common Equivalent Share, FY2025 |

## I — Inputs through the model

The model uses a flat **6.5583%** FCFF growth rate in each of Years 1-5, derived from Costco's FY2023-FY2025 net-sales CAGR. This is a forecast based on reported history, not company guidance.

Two inputs are not 10-K facts:

- **WACC: 10.0% placeholder — unresolved.** Costco's 10-K does not supply a market cost of equity, so a fully sourced WACC has not been established.
- **Terminal growth: 3.0% assumption.** This is a long-run macro assumption, not a Costco-specific disclosure.

With those inputs, the model produces:

| Output | Value |
|---|---:|
| Present value of explicit five-year FCFF | $36,181.4 |
| Present value of terminal value | $99,817.1 |
| Enterprise value | $135,998.5 |
| Equity value | $144,354.5 |
| Value per diluted share | **$324.54** |
| Terminal value as share of enterprise value | 73.4% |

## V — Value reasonableness

The most recent available COST quote was **$902.75 per share**, after-hours on September 9, 2026 at 7:59 PM EDT, retrieved September 10, 2026. The regular-session close was $902.60.

The model's $324.54 value per diluted share is **0.360x** that price, below the 0.5x reasonableness floor of $451.38. No inputs were adjusted merely to close that gap.

The input requiring the most work is WACC: it remains unresolved because the 10-K alone cannot establish Costco's market cost of equity. The terminal value's 73.4% share of enterprise value makes the valuation particularly sensitive to that discount rate.

## E — Examine sensitivity and reverse DCF

### Sensitivity grid: value per diluted share

| WACC / terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | $334.96 | $376.39 | $434.39 |
| 10% | $294.58 | $324.54 | $364.48 |
| 11% | $263.20 | $285.67 | $314.56 |

Value falls as WACC rises and rises as terminal growth rises. Even the most favorable displayed corner ($434.39) remains below the quoted $902.75 price.

### Reverse DCF

A reverse DCF begins with the market price and solves backward for the assumption needed to reach it. Holding starting FCFF, WACC, terminal growth, cash, debt, and diluted shares fixed, the model solves for one uniform shift added to all five explicit growth rates.

Within the required search bracket of **-5 to +10 percentage points**, the model reports **no solution**: the target price cannot be reached. An unconstrained diagnostic calculation would require a **+27.78-percentage-point** shift, making the Year 1-5 growth rates **34.34% each** rather than 6.5583% each. This is an implication of the held-fixed assumptions, not proof of mispricing.

## R — Recommendation and monitor

**Watch-defer. Initiate if COST falls below about $325 per share, where the price-implied uniform growth shift falls to the base forecast path, or if newly sourced evidence supports a materially higher FCFF growth path. Otherwise, defer.**

Monitor: **operating cash flow less capital expenditures in the next Form 10-Q**, because it directly refreshes the starting FCFF calculation.

## Sources

- Costco Wholesale Corporation, [FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm): Item 7; Consolidated Balance Sheets; Consolidated Statements of Cash Flows; Note 4; and Note 9.
- [COST market-price history](https://stockanalysis.com/stocks/cost/history/) for the separately identified quote.

---

*This post is for educational and informational purposes only. It is not financial, investment, legal, or tax advice, and it is not a recommendation to buy or sell any security. Verify source information independently and consult a qualified professional before making investment decisions.*
