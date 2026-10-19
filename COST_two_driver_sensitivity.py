"""Reproduce one-at-a-time COST operating sensitivities for FY2026–FY2030."""

import COST_three_statement_2026_2030 as model


CASES = (
    ("Base", None, None),
    ("Sales growth lower", "SALES_GROWTH", 0.05),
    ("Sales growth higher", "SALES_GROWTH", 0.07),
    ("Capex/sales lower", "CAPEX_TO_SALES", 0.018),
    ("Capex/sales higher", "CAPEX_TO_SALES", 0.022),
)


def run_case(name, input_name, value):
    previous = getattr(model, input_name) if input_name else None
    if input_name:
        setattr(model, input_name, value)
    try:
        rows = model.forecast()
        model.check(rows)
        final = rows[-1]
        # The model's valuation clips negative explicit-year FCFE. Do not use
        # that valuation convention if any case has a negative FCFE year.
        if any(row["fcfe"] < 0 for row in rows):
            per_share = "unavailable: negative FCFE year"
        else:
            equity_value = model.value_equity(rows)[-1]
            per_share = f"${equity_value / model.SHARES_MILLIONS:,.2f}"
        print(f"{name:<20} {final['ebit']:>15,.1f} {final['fcfe']:>15,.1f} {per_share:>24}")
    finally:
        if input_name:
            setattr(model, input_name, previous)


if __name__ == "__main__":
    print("COST one-at-a-time sensitivity | FY2026–FY2030 | USD millions except per share")
    print("Sales growth: 5% / 6% base / 7% each year")
    print("Capital spending / net sales: 1.8% / 2.0% base / 2.2% each year")
    print("Case                 FY2030 operating income       FY2030 FCFE          Value/share")
    for case in CASES:
        run_case(*case)
