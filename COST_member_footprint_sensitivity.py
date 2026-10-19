"""One-at-a-time COST paid-member and warehouse-footprint sensitivities."""

from COST_two_driver_sensitivity import run_case


CASES = (
    ("Base", None, None),
    ("Member growth lower", "PAID_MEMBER_GROWTH", 0.053),
    ("Member growth higher", "PAID_MEMBER_GROWTH", 0.073),
    ("Footprint lower", "WAREHOUSE_SQFT_PER_STORE", 146_000.0),
    ("Footprint higher", "WAREHOUSE_SQFT_PER_STORE", 148_000.0),
)


if __name__ == "__main__":
    print("COST one-at-a-time sensitivity | FY2026–FY2030 | USD millions except per share")
    print("Paid-member growth: 5.3% / 6.3% base / 7.3% each year")
    print("Warehouse footprint: 146,000 / 147,000 base / 148,000 square feet per warehouse")
    print("Case                 FY2030 operating income       FY2030 FCFE          Value/share")
    for case in CASES:
        run_case(*case)
