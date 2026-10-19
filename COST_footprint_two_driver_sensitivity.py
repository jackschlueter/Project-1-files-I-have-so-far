"""Run after partner review: COST footprint and capital-spending sensitivities."""

from COST_two_driver_sensitivity import run_case


CASES = (
    ("Base", None, None),
    ("Footprint lower", "WAREHOUSE_SQFT_PER_STORE", 146_000.0),
    ("Footprint higher", "WAREHOUSE_SQFT_PER_STORE", 148_000.0),
    ("Capex/sales lower", "CAPEX_TO_SALES", 0.018),
    ("Capex/sales higher", "CAPEX_TO_SALES", 0.022),
)


if __name__ == "__main__":
    print("COST one-at-a-time sensitivity | FY2026–FY2030 | USD millions except per share")
    print("Warehouse footprint: 146,000 / 147,000 base / 148,000 square feet per warehouse")
    print("Capital spending / net sales: 1.8% / 2.0% base / 2.2% each year")
    print("Case                 FY2030 operating income       FY2030 FCFE          Value/share")
    for case in CASES:
        run_case(*case)
