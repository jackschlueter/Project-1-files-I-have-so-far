# COST footprint and capital-spending sensitivity results

Run at **2026-09-29 21:05:47 UTC** with `python3 COST_footprint_two_driver_sensitivity.py`. The user said to skip the pending partner review. The earlier prediction remains in `COST_locked_footprint_record_2026-09-29.md`; no partner confirmation is claimed.

Each case changes **one independent input** in `COST_three_statement_2026_2030.py`. All other base inputs stay fixed. Forecast years are FY2026–FY2030. Currency is USD millions except value per share.

| Driver | Lower | Base | Higher | How applied | Reason for range |
| --- | ---: | ---: | ---: | --- | --- |
| Average warehouse footprint | 146,000 | 147,000 | 148,000 **square feet per warehouse** | Changed FY2026 fleet average scales the FY2026 net-sales level once; the effect carries through FY2030 | FY2025 10-K reports approximately 147,000 square feet per warehouse; ±1,000 square feet is a judgment, not company guidance. |
| Capital spending / net sales | 1.8% | 2.0% | 2.2% **per year** | Same percentage in each FY2026–FY2030 year | FY2025 capital spending was $5,498 million, about 2.04% of $269,912 million net sales; ±0.2 percentage point is a judgment. |

| Case | FY2030 operating income, USD m | FY2030 FCFE, USD m | Value/share, USD |
| --- | ---: | ---: | ---: |
| Base | 13,792.2 | 5,875.0 | $205.65 |
| Footprint lower: 146,000 sq ft/warehouse | 13,713.1 | 5,847.6 | $204.81 |
| Footprint higher: 148,000 sq ft/warehouse | 13,871.3 | 5,902.3 | $206.48 |
| Capital spending lower: 1.8% of sales | 13,792.2 | 6,426.8 | $220.99 |
| Capital spending higher: 2.2% of sales | 13,792.2 | 5,323.2 | $190.30 |

The model reports **free cash flow to equity (FCFE)** after scheduled debt repayment and a buyback that offsets stock compensation. Every case has positive FCFE in all five forecast years and passes the model's balance-sheet, cash, property, debt, equity, and minimum-cash checks. Value per share retains the base 10% cost of equity and 2.5% terminal growth assumptions.

The 148,000-square-foot result versus the base is **+$79.1 million** FY2030 operating income, **+$27.3 million** FY2030 FCFE, and **+$0.83/share**. That is within the locked rough prediction. The footprint link assumes unchanged sales per square foot and does **not** separately price the cost of enlarging warehouses; the value effect is therefore a narrow model scenario, not an investment estimate.
