# Asbury five-year classroom model

This is a classroom exercise. This is not investment advice.

USD millions except per-share figures. Run `python asbury_three_statement.py` in this folder to reproduce every figure below.

## Value and the three judgments

The supplied assumptions give an equity value of **$4,008.9 million**, or **$223.32 per share**, using free cash flow to equity (FCFE), a 10% cost of equity, a 2.5% perpetual growth rate, and the supplied 17.951349 million share count. This is a simplified beginning-of-2026 classroom valuation; the later share count is used solely as the case denominator.

1. **Gross margin: 17.05%.** ABG's FY2025 reported gross profit was $3,071.7 million on $17,999.0 million of sales. At 16.55% gross margin, modeled value is **$205.49/share**; at 17.55%, **$241.15/share**. Revenue grows 1.8% each year as instructed.
2. **SG&A leverage: 66.5% down to 64.5% of gross profit.** This is a forecast of operating efficiency. Raising each year's SG&A ratio by one percentage point lowers value to **$206.43/share**; lowering it by one point raises value to **$240.21/share**.
3. **The value assigned after 2030.** At 10% cost of equity and 2.5% terminal growth, the present value of the terminal period is **$2,924.6 million**, about 73% of modeled equity value. A 9% cost of equity raises value to **$258.85/share**; 11% lowers it to **$196.18/share**. A 2% or 3% terminal growth rate gives **$212.39** or **$235.81/share**.

These are one-at-a-time sensitivities, not probabilities or trading targets.

## Three statement links

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Revenue | 18,323.0 | 18,652.8 | 18,988.5 | 19,330.3 | 19,678.3 |
| Gross profit | 3,124.1 | 3,180.3 | 3,237.5 | 3,295.8 | 3,355.1 |
| Operating income | 844.2 | 890.3 | 938.1 | 954.5 | 971.4 |
| Net income | 416.0 | 455.2 | 495.5 | 512.5 | 529.8 |
| Operating cash flow | 613.8 | 657.4 | 702.1 | 723.3 | 744.6 |
| Investing cash flow | (250.0) | (250.0) | (250.0) | (250.0) | (250.0) |
| Financing cash flow | (300.0) | (300.0) | (300.0) | (300.0) | (300.0) |
| Ending cash | 104.2 | 211.7 | 363.8 | 537.0 | 731.7 |
| FCFE before buybacks | 213.8 | 257.4 | 302.1 | 323.3 | 344.6 |
| Balance-sheet check | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

Cash is calculated last: prior cash + operating cash flow + investing cash flow + financing cash flow. It is never used as a plug to make the balance sheet balance. The code independently checks both the cash roll-forward and **assets = liabilities + equity** for each of the five years. Inventory follows 52.2242 days of cost of sales; floor-plan debt follows 94.9059% of inventory. PP&E rolls forward with $250 million of capital spending less depreciation, and the $120 million annual non-cash impairment reduces other assets. Equity rolls forward with net income less $150 million annual buybacks. No revolver draw is needed in this base case; cash stays above the $25 million minimum.

## Model conventions and source check

- The case's rounded opening balance sheet implies **$3,891.7 million equity**. ABG's FY2025 Form 10-K reports **$3,891.9 million**. The $0.2 million difference comes from the case's aggregated `other liabilities` figure. The model uses the case aggregates so its opening balance sheet balances.
- Interest uses the average opening and closing floor-plan and term-debt balances. The revolver, if needed, is drawn to restore $25 million cash, subject to the $850 million limit.
- The terminal value grows 2030 FCFE by 2.5% in perpetuity. This assumes the modeled cash generation and $150 million annual term-debt repayment can continue after 2030; actual term debt would eventually be repaid, so the terminal value is a classroom simplification.
- The supplied **17,951,349** share count is used exactly. The [June 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1144980/000114498026000094/abg-20260630.htm) instead says **17,951,917 shares as of July 29, 2026**. The 568-share difference changes the modeled price by less than one cent.
- FY2025 revenue, cost of sales, depreciation, cash, inventory, PP&E, debt, and reported equity were checked against ABG's [FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1144980/000114498026000051/abg-20251231.htm). All forecast judgments are the supplied classroom assumptions.
