# Costco Wholesale (COST): individual three-statement valuation submission [^education]

**Basis:** FY2025 opening balance sheet; FY2026–FY2030 forecast. USD millions except per-share values. The executable model is [COST_three_statement_2026_2030.py](COST_three_statement_2026_2030.py).

**Filed sources:** [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm), [FY2024 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983224000049/cost-20240901.htm), [FY2023 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983223000042/cost-20230903.htm); the share denominator is from the [May 2026 10-Q](https://www.sec.gov/Archives/edgar/data/909832/000090983226000051/cost-20260510.htm). Historical filing amounts are observations; all forward assumptions labelled judgment below are my estimates.

## Opening balance sheet (FY2025, filed)

| Assets | $m | Liabilities and equity | $m |
| --- | ---: | --- | ---: |
| Cash | 14,161 | Accounts payable | 19,783 |
| Short-term investments | 1,123 | Accrued salaries and benefits | 5,205 |
| Receivables | 3,203 | Accrued member rewards | 2,677 |
| Merchandise inventories | 18,116 | Deferred membership fees | 2,854 |
| Other current assets | 1,777 | Other current liabilities, excluding current debt | 6,514 |
| PP&E, net | 31,909 | Debt, net carrying amount | 5,788 |
| Operating lease ROU assets | 2,725 | Long-term operating lease liabilities | 2,460 |
| Other long-term assets | 4,085 | Other long-term liabilities | 2,654 |
| **Total assets** | **77,099** | **Total liabilities** | **47,935** |
| | | **Equity** | **29,164** |
| | | **Liabilities + equity** | **77,099** |

The [FY2025 balance sheet](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) reports $6,589 of other current liabilities and $5,713 of long-term debt. [Note 4](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) says $75 of current debt is included in other current liabilities; I move that $75 into the model's debt line, preserving both filed totals.

## Assumptions

| Value | Label | Reason |
| --- | --- | --- |
| FY2025 net sales $269,912; membership fees $5,323 | History | Filed FY2025 income statement; the model forecasts these separately. |
| FY2025 balance-sheet components above | History | Filed FY2025 balance sheet and debt note; opening assets equal liabilities plus equity without a plug. |
| FY2025 merchandise gross margin 11.12%; SG&A / calculated gross profit 70.63% | History | Calculated from filed net sales, merchandise costs, membership fees, and SG&A. |
| 2026–2030 net-sales growth 6% per year | Judgment | FY2025 comparable sales rose 6%, versus 8.1% total net-sales growth; I use the lower pace rather than repeat all new-store contribution. |
| 2026–2030 membership-fee growth 7% per year | Judgment | Paid-member growth and Executive upgrades can lift fees, but I do not assume a new fee increase each year; this is Costco's named business driver. |
| Merchandise gross margin 11.1% | Judgment | Holds near FY2025's 11.12% without assuming sustained pricing improvement. |
| SG&A / calculated gross profit 71% | Judgment | Near FY2025's 70.63%; Costco's past cost-ratio improvement is not extended indefinitely. |
| Inventory days 28, using ending inventory and 365 days | Judgment | Near the FY2025 inventory level relative to merchandise costs, with a simple constant turnover rule. |
| Depreciation and amortization 7.6% of opening net PP&E | Judgment | Near FY2025 D&A divided by year-end net PP&E; treated as a PP&E reduction for this simplified forecast. |
| Cash capital spending 2.0% of net sales | Judgment | Close to FY2025 cash additions to PP&E of $5,498 / $269,912 of net sales. |
| Effective tax rate 25% | Judgment | Near the three observed FY2023–FY2025 effective rates; losses, if any, receive no assumed tax benefit. |
| Receivables, other current assets, accrued payroll, member rewards, other current liabilities: FY2025 ratios to net sales | Judgment | Without a separate company forecast for each account, I hold their latest filed relationship to sales fixed. |
| Accounts payable: FY2025 ratio to merchandise costs; deferred fees: FY2025 ratio to membership fees | Judgment | These bases match the activities that chiefly generate the balances. |
| Stock compensation: FY2025 rate of $860 / net sales; equal maintenance buybacks | Judgment | Carries forward the latest noncash compensation intensity and uses cash buybacks to approximately hold the share count constant. |
| Debt repayment: $75, $2,250, $0, $148, $1,750 in FY2026–2030 | History | Contractual maturity schedule disclosed in FY2025 10-K Note 4; the model uses net carrying debt and no new issuance. |
| No new debt or revolver draw | Judgment | Opening cash and modeled operating cash cover scheduled debt repayments while retaining the $10,000 cash floor. |
| Debt interest: 2.66% of average net debt | Judgment | FY2025 interest expense of $154 divided by opening net carrying debt of $5,788; applied to average forecast debt. |
| Short investments, lease assets/liabilities, and other long-term assets/liabilities held flat | Judgment | No sourced transaction or lease schedule supports a more detailed five-year change; this is a model limit. |
| Minimum cash $10,000 | Judgment | Close to FY2024 year-end cash of $9,906; retained as an operating liquidity floor. |
| Cost of equity 10%; terminal growth 2.5% | Judgment | Classroom valuation scenario; growth remains below the discount rate. These two inputs strongly affect terminal value. |
| 443.514 million shares | History | Shares outstanding in the May 2026 10-Q; used for the one per-share value. |
| Floor-plan borrowing: none | History | Costco is a membership-warehouse retailer; the FY2025 filed balance sheet has no auto-dealer inventory floor-plan line. Membership fees are the named differentiating line. |

## Five-year income statement

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Net sales | 286,106.7 | 303,273.1 | 321,469.5 | 340,757.7 | 361,203.1 |
| Membership fees | 5,695.6 | 6,094.3 | 6,520.9 | 6,977.4 | 7,465.8 |
| Total revenue | 291,802.3 | 309,367.4 | 327,990.4 | 347,735.0 | 368,668.9 |
| Merchandise costs | 254,348.9 | 269,609.8 | 285,786.4 | 302,933.6 | 321,109.6 |
| Calculated gross profit | 37,453.5 | 39,757.6 | 42,204.0 | 44,801.5 | 47,559.3 |
| SG&A | 26,592.0 | 28,227.9 | 29,964.9 | 31,809.0 | 33,767.1 |
| Operating income | 10,861.5 | 11,529.7 | 12,239.2 | 12,992.4 | 13,792.2 |
| Interest expense | 153.0 | 122.1 | 92.1 | 90.2 | 64.9 |
| Pretax income | 10,708.5 | 11,407.6 | 12,147.0 | 12,902.3 | 13,727.3 |
| Income tax | 2,677.1 | 2,851.9 | 3,036.8 | 3,225.6 | 3,431.8 |
| Net income | 8,031.4 | 8,555.7 | 9,110.3 | 9,676.7 | 10,295.5 |

Costco reports depreciation within operating expense categories; it is not subtracted a second time below SG&A.

## Five-year balance sheet

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cash | 19,382.1 | 23,198.5 | 29,769.3 | 36,698.1 | 42,573.1 |
| Short investments | 1,123.0 | 1,123.0 | 1,123.0 | 1,123.0 | 1,123.0 |
| Receivables | 3,395.2 | 3,598.9 | 3,814.8 | 4,043.7 | 4,286.3 |
| Inventory | 19,511.7 | 20,682.4 | 21,923.3 | 23,238.7 | 24,633.1 |
| Other current assets | 1,883.6 | 1,996.6 | 2,116.4 | 2,243.4 | 2,378.0 |
| PP&E, net | 35,206.1 | 38,595.9 | 42,092.0 | 45,708.1 | 49,458.4 |
| ROU assets | 2,725.0 | 2,725.0 | 2,725.0 | 2,725.0 | 2,725.0 |
| Other long assets | 4,085.0 | 4,085.0 | 4,085.0 | 4,085.0 | 4,085.0 |
| **Total assets** | 87,311.6 | 96,005.3 | 107,648.8 | 119,865.1 | 131,261.9 |
| Accounts payable | 20,975.7 | 22,234.3 | 23,568.3 | 24,982.4 | 26,481.4 |
| Accrued payroll | 5,517.3 | 5,848.3 | 6,199.2 | 6,571.2 | 6,965.5 |
| Member rewards | 2,837.6 | 3,007.9 | 3,188.3 | 3,379.7 | 3,582.4 |
| Deferred membership fees | 3,053.8 | 3,267.5 | 3,496.3 | 3,741.0 | 4,002.9 |
| Other current liabilities | 6,904.8 | 7,319.1 | 7,758.3 | 8,223.8 | 8,717.2 |
| Debt, net carrying amount | 5,713.0 | 3,463.0 | 3,463.0 | 3,315.0 | 1,565.0 |
| Lease liabilities | 2,460.0 | 2,460.0 | 2,460.0 | 2,460.0 | 2,460.0 |
| Other long liabilities | 2,654.0 | 2,654.0 | 2,654.0 | 2,654.0 | 2,654.0 |
| **Total liabilities** | 50,116.3 | 50,254.2 | 52,787.5 | 55,327.1 | 56,428.4 |
| **Equity** | 37,195.4 | 45,751.1 | 54,861.4 | 64,538.1 | 74,833.5 |

## Five-year cash-flow statement

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Net income | 8,031.4 | 8,555.7 | 9,110.3 | 9,676.7 | 10,295.5 |
| Depreciation added back | 2,425.1 | 2,675.7 | 2,933.3 | 3,199.0 | 3,473.8 |
| Stock compensation added back | 911.6 | 966.3 | 1,024.3 | 1,085.7 | 1,150.9 |
| Increase in operating assets | 1,694.5 | 1,487.4 | 1,576.7 | 1,671.3 | 1,771.6 |
| Increase in operating liabilities | 2,256.3 | 2,387.9 | 2,533.3 | 2,687.6 | 2,851.3 |
| **Operating cash flow** | 11,929.8 | 13,098.1 | 14,024.5 | 14,977.7 | 15,999.9 |
| Capital spending | -5,722.1 | -6,065.5 | -6,429.4 | -6,815.2 | -7,224.1 |
| Debt repayment | -75.0 | -2,250.0 | 0.0 | -148.0 | -1,750.0 |
| Maintenance share buyback | -911.6 | -966.3 | -1,024.3 | -1,085.7 | -1,150.9 |
| **Financing cash flow** | -986.6 | -3,216.3 | -1,024.3 | -1,233.7 | -2,900.9 |
| Change in cash | 5,221.1 | 3,816.4 | 6,570.8 | 6,928.8 | 5,875.0 |
| **Ending cash** | 19,382.1 | 23,198.5 | 29,769.3 | 36,698.1 | 42,573.1 |
| FCFE after maintenance buyback | 5,221.1 | 3,816.4 | 6,570.8 | 6,928.8 | 5,875.0 |

The increase in operating assets is a **cash use** in operating cash flow; the increase in operating liabilities is a **cash source**.

## Checks

| USD millions | 2026 | 2027 | 2028 | 2029 | 2030 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Assets − liabilities − equity | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash roll-forward gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| PP&E roll-forward gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt roll-forward gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Equity roll-forward gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash above $10,000 floor | 9,382.1 | 13,198.5 | 19,769.3 | 26,698.1 | 32,573.1 |

All reconciliation gaps are zero at displayed precision; the executable model enforces a $0.0000001 million tolerance. Cash remains above the floor in every year, so no revolver draw occurs. Every forecast FCFE is positive.

## One value per share

Discounting positive FY2026–FY2030 FCFE at 10% gives **$21,217.6 million**; the terminal period contributes **$64,704.8 million** after normalizing FY2030's scheduled debt repayment so it is not repeated forever. Adding **$5,284.0 million** of opening cash above the floor and short investments gives **$91,206.4 million of equity value, or $205.65 per share** on 443.514 million shares. This is a scenario output, not a recommendation.

## Partner-style attack and two-sentence answer

**Attack:** Your 7% membership-fee growth assumes no further fee increase, but Costco says the FY2025 fee increase produced about 40% of that year's membership-income growth. What paid-member, renewal, and Executive-upgrade path supplies 7% each year, and what reported result would make you lower it?

**Answer:** I used 7% because FY2025 fee revenue grew 10.3% and roughly 40% of its dollar increase came from the fee increase, leaving about 6.2% growth from other drivers; my forecast asks for a modest improvement from those drivers. I would lower it if reported fee growth without a new price increase stays below 7% or renewal and Executive-upgrade trends weaken, and raise it only if sustained filings show stronger member growth.

The fee-growth figures and fee-increase contribution come from [FY2025 10-K Item 7](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm). This challenge is drafted for the class exchange; it is not attributed to an actual partner.

[^education]: This classroom model is for educational use only and is not investment advice.
