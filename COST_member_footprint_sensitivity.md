# COST: paid-member growth and warehouse footprint

Reproduce with `python3 COST_member_footprint_sensitivity.py` in this folder. The two drivers are **independent model inputs** and are changed **one at a time**. Forecast years are FY2026–FY2030. Money is **USD millions** except value per share.

| Driver | Lower | Base | Higher | Applied years and range reason |
| --- | ---: | ---: | ---: | --- |
| `PAID_MEMBER_GROWTH` | 5.3% | 6.3% | 7.3% **per year** | Same rate in each FY2026–FY2030 year. Costco's paid memberships rose from 76.2 million in FY2024 to 81.0 million in FY2025, about 6.3%; FY2023–FY2024 growth was about 7.3%. The 5.3% lower case is a labeled judgment. Changes are ±1 **percentage point**, not ±1% of the rate. |
| `WAREHOUSE_SQFT_PER_STORE` | 146,000 | 147,000 | 148,000 **square feet per warehouse** | Change the fleet-average space in FY2026; its sales-level effect carries through FY2030, without repeating the size shock each year. Costco reports approximately 147,000 square feet per warehouse and says newer units are slightly larger. The ±1,000-square-foot range is a labeled judgment. |

History source: [Costco FY2025 Form 10-K, Items 1 and 7](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm).

## Same outputs in every run

| Case | FY2030 paid members, millions | FY2030 operating income, USD m | FY2030 FCFE, USD m | Model value/share, USD |
| --- | ---: | ---: | ---: | ---: |
| Base | 109.94 | 13,792.2 | 5,875.0 | $205.65 |
| Member growth lower: 5.3% yearly | 104.86 | 13,155.6 | 5,481.3 | $195.92 |
| Member growth higher: 7.3% yearly | 115.21 | 14,453.3 | 6,289.2 | $215.83 |
| Footprint lower: 146,000 sq ft/warehouse | 109.94 | 13,713.1 | 5,847.6 | $204.81 |
| Footprint higher: 148,000 sq ft/warehouse | 109.94 | 13,871.3 | 5,902.3 | $206.48 |

The model uses **free cash flow to equity (FCFE)** after scheduled debt repayment and a buyback assumed to offset stock compensation. All five cases have positive FCFE in every forecast year and pass the balance-sheet, cash, property, debt, equity, and minimum-cash checks.

## What creates the effects

The base 6% net-sales and 7% membership-fee growth forecasts already assume normal member growth. To avoid counting the **base** member growth twice, the model applies only a *relative scenario factor* each year: `(1 + tested member growth) / (1 + 6.3%)`. That factor changes both forecast sales and fees, assuming the same sales and fee yield per paid membership relative to the base. More members therefore raise merchandise gross profit and fee revenue, partly offset by working capital and capital spending. The proportional link is a judgment; Costco has not reported a one-for-one elasticity.

The footprint case scales FY2026 merchandise sales once by `tested square feet / 147,000`, then retains the normal growth path. Membership fees and paid-member counts stay fixed. A larger warehouse is assumed to sell more merchandise at unchanged sales per square foot. The model does not separately add the cost of building more space, so this footprint sensitivity can overstate the net benefit of expansion.

The model value/share uses 10% cost of equity and 2.5% terminal growth. These are illustrative outputs from the FY2025-based classroom model, **not updated current valuations**. Costco's September 24, 2026 operating-results release reports FY2026 net sales of **$297.247 billion**, while this older model forecast **$286.107 billion** for FY2026; the new actual would require a full model rebase before a current valuation. [Costco FY2026 operating results](https://investor.costco.com/news/news-details/2026/Costco-Wholesale-Corporation-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Operating-Results/default.aspx)
