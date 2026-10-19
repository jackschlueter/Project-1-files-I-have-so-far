# Costco DCF inputs

Costco Wholesale Corporation (NASDAQ: COST). Latest Form 10-K: fiscal year ended August 31, 2025.

| Input | Value | Unit | As-of date | Source locator |
|---|---:|---|---|---|
| Starting FCFF | 7,952.3 | USD millions | FY ended Aug. 31, 2025 | Cash Flow Statement: CFO 13,335 + after-tax interest [154 x (1 - 25.1%)] - additions to property and equipment 5,498. [SEC 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) |
| Growth, Years 1-5 | 6.5583%, 6.5583%, 6.5583%, 6.5583%, 6.5583% | Percent | Forecast from FY2025 | Uniform forecast equal to the FY2023-FY2025 net-sales CAGR: ($269,912m / $237,710m)^(1/2) - 1. Both sales figures are in Item 7. [SEC 10-K, Item 7](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) |
| WACC | 10.0% **(placeholder—unresolved)** | Percent | Model placeholder | Costco's 10-K reports debt and interest expense, but does not provide the market cost of equity needed for a sourced WACC. The required training value remains until market-derived inputs are sourced. |
| Terminal growth | 3.0% | Percent | Long-run assumption | Macro-based assumption; CBO's long-run nominal GDP range is 2.7% to 5.1% by 2036. [CBO outlook](https://www.cbo.gov/publication/62105) |
| Cash / debt / diluted shares | 14,161 / 5,805 / 444.803 | USD millions / USD millions / millions | Aug. 31, 2025 / FY2025 | Balance Sheet cash and cash equivalents; Note 4 total long-term debt; Note 9 weighted-average diluted shares. [SEC 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) |

## Market price

Most recent available COST quote: **$902.75 per share**, after-hours, **September 9, 2026, 7:59 PM EDT** (retrieved September 10, 2026). Regular-session close: $902.60. [StockAnalysis](https://stockanalysis.com/stocks/cost/history/)

## Reasonableness

The DCF value is **$324.54 per diluted share** versus the most recent available price of **$902.75**: **0.360x** price. This is outside the 0.5x–2.0x range (lower bound: $451.38). Inputs were not adjusted.

The input I distrust most is the **10.0% WACC placeholder**. It is unresolved because Costco's 10-K does not provide the market cost of equity. It is especially consequential here because the terminal value supplies 73.4% of enterprise value.

## Sensitivity grid and reverse DCF

| WACC / terminal growth | 2% | 3% | 4% |
|---|---:|---:|---:|
| 9% | $334.96 | $376.39 | $434.39 |
| 10% | $294.58 | $324.54 | $364.48 |
| 11% | $263.20 | $285.67 | $314.56 |

At the $902.75 target price, the required uniform increase to the five explicit growth rates is **+27.78 percentage points**, implying a 34.34% rate in each of Years 1-5. This is outside the prescribed -5 to +10 percentage-point reverse-DCF search bracket; `dcf.py` therefore correctly reports no solution in that bracket. The reverse calculation holds starting FCFF, WACC, terminal growth, cash, debt, and diluted shares fixed.

## Conditional call

**Watch-defer. Initiate if COST falls below about $325 per share, where the price-implied uniform growth shift falls to my base forecast path, or if newly sourced evidence supports a materially higher FCFF growth path. Otherwise, defer.**

Monitor: **operating cash flow less capital expenditures in the next Form 10-Q**, because it directly updates starting FCFF.
