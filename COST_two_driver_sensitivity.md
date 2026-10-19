# COST: two operating input sensitivities

Run `python3 COST_two_driver_sensitivity.py` in this folder. This imports the unchanged linked model in `COST_three_statement_2026_2030.py` and changes one input at a time; all other base inputs stay fixed. Forecast years are FY2026–FY2030. Currency is USD millions except value per share.

## Inputs and ranges

| Independent model input | Lower | Base | Higher | Affected years | Range reason |
| --- | ---: | ---: | ---: | --- | --- |
| `SALES_GROWTH`, annual net-sales growth | 5% | 6% | 7% | Same rate in each FY2026–FY2030 year | **History anchor, judgment range:** FY2025 comparable sales contributed 6% growth, while total net sales grew about 8%, partly from new warehouses. The model uses 6% as a steadier base; ±1 **percentage point** tests weaker or stronger growth. |
| `CAPEX_TO_SALES`, annual capital spending / net sales | 1.8% | 2.0% | 2.2% | Same rate in each FY2026–FY2030 year | **History anchor, judgment range:** FY2025 capital spending was $5,498 million, about 2.04% of $269,912 million net sales. The ±0.2 **percentage point** cases bracket the 2% model input. At the model's FY2026 sales, the higher case is about $6,294 million, within the FY2025 filing's stated $6,000–$6,500 million FY2026 spending intention; the lower case is a downside-to-spending stress, not guidance. |

History source: saved [Costco FY2025 Form 10-K](COST_2025_10-K.md), Item 7, Net Sales and Capital Expenditure Plans. The ranges are classroom judgments, not Costco forecasts.

## Comparable outputs

| Case | FY2030 operating income, USD m | FY2030 FCFE, USD m | Value/share, USD |
| --- | ---: | ---: | ---: |
| Base: 6% sales growth; 2.0% capital spending / sales | 13,792.2 | 5,875.0 | $205.65 |
| Sales growth lower: 5% | 13,254.0 | 5,601.5 | $198.86 |
| Sales growth higher: 7% | 14,351.1 | 6,163.1 | $212.76 |
| Capital spending lower: 1.8% of sales | 13,792.2 | 6,426.8 | $220.99 |
| Capital spending higher: 2.2% of sales | 13,792.2 | 5,323.2 | $190.30 |

The model uses **FCFE**, defined here as operating cash flow minus capital spending, scheduled debt repayment, and the buyback assumed to offset stock compensation. All forecast-year FCFE values are positive in all five cases. The balance sheet, cash, property, debt, and equity roll-forward checks pass in every case, and cash stays above the $10,000 million minimum.

Higher sales growth raises merchandise gross profit and operating income, but also raises inventory, receivables, capital spending, and the buyback linked to stock compensation. Higher capital spending directly reduces FCFE. In this simplified model, capital spending does not change operating income within the five years because SG&A already includes depreciation and is calculated as a fixed share of gross profit; property and subsequent depreciation still roll forward in the cash-flow and balance-sheet schedules.

Value/share uses the model's 10% cost of equity and 2.5% terminal growth. The terminal calculation adds back the scheduled FY2030 $1,750 million debt repayment so that one maturity is not repeated forever. This terminal convention and the discount assumptions are material valuation judgments. No negative FCFE was discarded in these five cases.
