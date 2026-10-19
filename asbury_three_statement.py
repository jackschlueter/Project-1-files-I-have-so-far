"""ABG classroom three-statement forecast and equity cash-flow valuation.

USD millions except per-share figures. The FY2025 opening balance sheet is
the simplified, rounded case balance sheet supplied with the assignment.
This is a classroom exercise. This is not investment advice.
"""

YEARS = range(2026, 2031)
REVENUE_GROWTH = 0.018
GROSS_MARGIN = 0.1705
SGA_TO_GROSS_PROFIT = (0.665, 0.655, 0.645, 0.645, 0.645)
DEPRECIATION_RATE = 82.4 / 3070.4
ANNUAL_IMPAIRMENT = 120.0
ANNUAL_CAPEX = 250.0
TAX_RATE = 0.255
INVENTORY_DAYS = 2135.8 / (17999.0 - 3071.7) * 365
FLOOR_PLAN_TO_INVENTORY = 2027.0 / 2135.8
OTHER_WORKING_CAPITAL_RATE = 0.008
MINIMUM_CASH = 25.0
REVOLVER_LIMIT = 850.0
REVOLVER_RATE = 0.06
ANNUAL_TERM_REPAYMENT = 150.0
ANNUAL_BUYBACK = 150.0
FLOOR_PLAN_RATE = 0.0467
TERM_DEBT_RATE = 0.0544
COST_OF_EQUITY = 0.10
TERMINAL_GROWTH = 0.025
SHARES_MILLIONS = 17.951349

OPENING = {
    "revenue": 17999.0,
    "inventory": 2135.8,
    "ppe": 3070.4,
    "other_assets": 6371.6,
    "cash": 40.4,
    "floor_plan": 2027.0,
    "term_debt": 3572.0,
    "other_liabilities": 2127.5,
}
OPENING["equity"] = (
    OPENING["inventory"] + OPENING["ppe"] + OPENING["other_assets"]
    + OPENING["cash"] - OPENING["floor_plan"] - OPENING["term_debt"]
    - OPENING["other_liabilities"]
)


def forecast(gross_margin=GROSS_MARGIN, sga_rate_shift=0.0):
    prior = OPENING.copy()
    prior["revolver"] = 0.0
    rows = []
    for year, sga_rate in zip(YEARS, SGA_TO_GROSS_PROFIT):
        revenue = prior["revenue"] * (1 + REVENUE_GROWTH)
        cost_of_sales = revenue * (1 - gross_margin)
        gross_profit = revenue - cost_of_sales
        sga = gross_profit * (sga_rate + sga_rate_shift)
        depreciation = prior["ppe"] * DEPRECIATION_RATE
        impairment = ANNUAL_IMPAIRMENT
        ebit = gross_profit - sga - depreciation - impairment

        inventory = cost_of_sales * INVENTORY_DAYS / 365
        floor_plan = inventory * FLOOR_PLAN_TO_INVENTORY
        term_repayment = min(ANNUAL_TERM_REPAYMENT, prior["term_debt"])
        term_debt = prior["term_debt"] - term_repayment
        floor_interest = (prior["floor_plan"] + floor_plan) / 2 * FLOOR_PLAN_RATE
        term_interest = (prior["term_debt"] + term_debt) / 2 * TERM_DEBT_RATE
        # The revolver is checked after cash flows are calculated. A draw
        # would incur a full year of interest, solved algebraically below.
        interest_before_revolver = floor_interest + term_interest
        pretax_before_revolver = ebit - interest_before_revolver
        if pretax_before_revolver <= 0:
            raise ValueError("A tax-loss carryforward rule is needed.")

        other_wc_increase = (revenue - prior["revenue"]) * OTHER_WORKING_CAPITAL_RATE
        other_assets = prior["other_assets"] + other_wc_increase - impairment
        ppe = prior["ppe"] + ANNUAL_CAPEX - depreciation
        inventory_increase = inventory - prior["inventory"]
        floor_plan_increase = floor_plan - prior["floor_plan"]

        def calculate(revolver_draw):
            revolver = prior["revolver"] + revolver_draw
            revolver_interest = (prior["revolver"] + revolver) / 2 * REVOLVER_RATE
            pretax = pretax_before_revolver - revolver_interest
            tax = pretax * TAX_RATE
            net_income = pretax - tax
            cfo = (net_income + depreciation + impairment - inventory_increase
                   - other_wc_increase + floor_plan_increase)
            cfi = -ANNUAL_CAPEX
            cff = -term_repayment - ANNUAL_BUYBACK + revolver_draw
            cash = prior["cash"] + cfo + cfi + cff
            return revolver, revolver_interest, pretax, tax, net_income, cfo, cfi, cff, cash

        base = calculate(0.0)
        draw = 0.0
        if base[-1] < MINIMUM_CASH:
            # One dollar of new borrowing contributes one dollar of cash
            # less its after-tax average-balance interest cost.
            cash_per_draw = 1 - REVOLVER_RATE / 2 * (1 - TAX_RATE)
            draw = (MINIMUM_CASH - base[-1]) / cash_per_draw
            if prior["revolver"] + draw > REVOLVER_LIMIT:
                raise ValueError(f"{year}: revolver limit insufficient for minimum cash")
        revolver, revolver_interest, pretax, tax, net_income, cfo, cfi, cff, cash = calculate(draw)
        equity = prior["equity"] + net_income - ANNUAL_BUYBACK
        assets = cash + inventory + ppe + other_assets
        liabilities_and_equity = floor_plan + term_debt + revolver + prior["other_liabilities"] + equity
        balance_check = assets - liabilities_and_equity
        cash_check = cash - (prior["cash"] + cfo + cfi + cff)
        if abs(balance_check) > 1e-8 or abs(cash_check) > 1e-8:
            raise AssertionError(f"{year}: model does not reconcile")
        row = dict(year=year, revenue=revenue, cost_of_sales=cost_of_sales,
                   gross_profit=gross_profit, sga=sga, depreciation=depreciation,
                   impairment=impairment, ebit=ebit, floor_interest=floor_interest,
                   term_interest=term_interest, revolver_interest=revolver_interest,
                   pretax=pretax, tax=tax, net_income=net_income, cfo=cfo, cfi=cfi,
                   cff=cff, cash=cash, inventory=inventory, ppe=ppe,
                   other_assets=other_assets, floor_plan=floor_plan, term_debt=term_debt,
                   revolver=revolver, other_liabilities=prior["other_liabilities"],
                   equity=equity, assets=assets, liabilities_and_equity=liabilities_and_equity,
                   balance_check=balance_check, cash_check=cash_check,
                   # FCFE is cash available to owners before the discretionary
                   # buyback. Floor-plan changes are already in operating cash.
                   fcfe=cfo + cfi - term_repayment + draw)
        rows.append(row)
        prior = row
    return rows


def value_equity(rows, cost_of_equity=COST_OF_EQUITY, terminal_growth=TERMINAL_GROWTH):
    if terminal_growth >= cost_of_equity:
        raise ValueError("Terminal growth must be below cost of equity")
    pv_explicit = sum(r["fcfe"] / (1 + cost_of_equity) ** i
                      for i, r in enumerate(rows, 1))
    terminal_value = rows[-1]["fcfe"] * (1 + terminal_growth) / (cost_of_equity - terminal_growth)
    pv_terminal = terminal_value / (1 + cost_of_equity) ** len(rows)
    # Cash above the minimum is retained by the model and is distributable
    # in addition to its future FCFE. Count only the opening excess cash.
    opening_excess_cash = max(0, OPENING["cash"] - MINIMUM_CASH)
    equity_value = pv_explicit + pv_terminal + opening_excess_cash
    return pv_explicit, pv_terminal, opening_excess_cash, equity_value, equity_value / SHARES_MILLIONS


def main():
    rows = forecast()
    print("ABG classroom forecast | USD millions except per share")
    print(f"Opening equity from case aggregates: {OPENING['equity']:.1f}")
    print(f"Inventory days: {INVENTORY_DAYS:.4f}; floor-plan / inventory: {FLOOR_PLAN_TO_INVENTORY:.4%}")
    fields = ("revenue", "gross_profit", "ebit", "net_income", "cfo", "cfi", "cff",
              "cash", "inventory", "ppe", "floor_plan", "term_debt", "revolver",
              "equity", "fcfe", "balance_check")
    print("Line".ljust(24) + "".join(f"{r['year']:>12}" for r in rows))
    for field in fields:
        print(field.replace("_", " ").ljust(24) + "".join(f"{r[field]:>12.1f}" for r in rows))
    explicit, terminal, excess, equity, per_share = value_equity(rows)
    print(f"PV 2026-2030 FCFE: {explicit:.1f}")
    print(f"PV terminal FCFE: {terminal:.1f}")
    print(f"Opening excess cash: {excess:.1f}")
    print(f"Equity value: {equity:.1f}")
    print(f"Value per share: ${per_share:.2f}")
    print("One-at-a-time value sensitivity ($/share):")
    for label, changed_rows, ke, growth in (
        ("Gross margin 16.55%", forecast(gross_margin=0.1655), COST_OF_EQUITY, TERMINAL_GROWTH),
        ("Gross margin 17.55%", forecast(gross_margin=0.1755), COST_OF_EQUITY, TERMINAL_GROWTH),
        ("SG&A/GP +1 point", forecast(sga_rate_shift=0.01), COST_OF_EQUITY, TERMINAL_GROWTH),
        ("SG&A/GP -1 point", forecast(sga_rate_shift=-0.01), COST_OF_EQUITY, TERMINAL_GROWTH),
        ("Cost of equity 9%", rows, 0.09, TERMINAL_GROWTH),
        ("Cost of equity 11%", rows, 0.11, TERMINAL_GROWTH),
        ("Terminal growth 2%", rows, COST_OF_EQUITY, 0.02),
        ("Terminal growth 3%", rows, COST_OF_EQUITY, 0.03),
    ):
        print(f"  {label}: ${value_equity(changed_rows, ke, growth)[-1]:.2f}")


if __name__ == "__main__":
    main()
