# Locked Changed-Input Record — COST warehouse footprint

**Locked at:** 2026-09-29 21:03:08 UTC. **Status:** prediction recorded; the changed-footprint case has not been run. This supersedes the proposed sales-growth change in `COST_locked_changed_input_record_2026-09-29.md`, which remains as the earlier record.

## Prediction to show the partner before the run

| Item | Locked entry |
| --- | --- |
| Company and model | Costco (`COST`), `COST_three_statement_2026_2030.py` |
| One independent input | `WAREHOUSE_SQFT_PER_STORE`, fleet-average physical warehouse space |
| Old → new | **147,000 → 148,000 square feet per warehouse**, an increase of **1,000 square feet per warehouse** or about **0.68%** |
| Lower / base / higher | **146,000 / 147,000 / 148,000 square feet per warehouse**; the ±1,000-square-foot range is a labeled judgment around the FY2025 10-K's approximate 147,000-square-foot average |
| Affected forecast years | Set the new average for FY2026; its one-time sales-level effect carries through FY2027–FY2030. It is **not** a 0.68% increase compounded separately in each year |
| Controls | Keep annual sales growth at 6% and all other independent model inputs, including membership-fee growth, margin, SG&A/gross profit, capital spending/net sales, discount rate, terminal growth, debt schedule, and shares, at base values |
| Expected FY2030 operating income | **Up roughly $80 million**, from $13,792 million to about **$13,870 million** |
| Expected FY2030 FCFE | **Up roughly $20–$30 million**, from $5,875 million to about **$5,900 million** |
| Expected value per share | **Up roughly $0–$2/share**, from $205.65 to about **$206–$208/share** |
| Why | At fixed warehouse count and assumed constant merchandise sales per square foot, 1,000 more square feet per warehouse raises the modeled sales level by about 0.68%. Merchandise gross profit and operating income rise; extra inventory, receivables, and capital spending offset part of the cash benefit. |

Amounts are **USD millions** unless stated as **USD per share**. These are rough predictions from the model's formulas and previous base output, not results from a 148,000-square-foot run. The filed 147,000-square-foot figure is approximate. The ±1,000-square-foot range and constant sales productivity are judgments; the model does not separately price construction needed to expand the fleet.

## Listener check — complete before either new case is run

- Partner has seen the prediction, **square feet per warehouse** units, 146,000–148,000 range, and FY2026–FY2030 effect: **pending**.
- Partner confirms **1,000 square feet per warehouse** is an absolute area change, while **0.68%** is the relative change: **pending**.
- Partner confirms only `WAREHOUSE_SQFT_PER_STORE` changes and the effect is applied once to the FY2026 sales level: **pending**.
- Unclear unit or range and resolution: **pending partner review**.
- Partner's own locked input prediction and ranges shown to me before their run: **pending exchange**.
- My unit and one-input check of the partner's prediction: **pending exchange**.

Record actual partner answers here before running the changed-footprint case. Do not fill in confirmations without the partner.

## Post-run result added 2026-09-29 21:34:25 UTC

The pending status above describes the record **at lock time**. The user later said to skip that review and authorized the run. A later isolated rerun in `COST_proforma_sensitivity.py` confirmed the result with a fresh copy of the saved base inputs for each case.

| Output | Locked prediction | Actual base | Actual 148,000 sq ft/warehouse | Actual change from displayed base |
| --- | ---: | ---: | ---: | ---: |
| FY2030 operating income, USD millions | About +80 | 13,792.2 | 13,871.3 | +79.1 |
| FY2030 FCFE, USD millions | +20 to +30 | 5,875.0 | 5,902.3 | +27.3 |
| Model value, USD/share | +0 to +2 | $205.65 | $206.48 | +$0.83 |

**Prediction error:** Operating-income change was $0.9 million below the rough +$80 million prediction. The FCFE and per-share results fall inside the predicted ranges. The small operating-income difference reflects the rough rounding in the prediction; the actual linked model applies 11.1% merchandise margin and 71% SG&A/gross profit to the sales change. The FCFE result also includes recalculated working capital, capital spending, and the stock-compensation offset buyback.

**Conclusion and research priority:** This result does not change the classroom valuation conclusion: the modeled per-share movement is $0.83 from a $205.65 base, and the footprint scenario omits a separate construction cost. The research priority remains validating the assumed paid-member-to-sales/fees link and rebasing the FY2025-opening model to reported FY2026 results before treating any per-share figure as current. [Costco FY2026 operating-results release](https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Operating-Results/default.aspx).

All five forecast years in the base and changed-footprint case passed the balance-sheet, cash, property, debt, equity, and minimum-cash checks. The original prediction has not been edited.
