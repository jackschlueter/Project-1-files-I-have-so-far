"""Asbury Automotive Group five-year pro forma (USD millions).

This is a classroom exercise. This is not investment advice.
"""

YEARS = range(2026, 2031)

# Case assumptions. Historical ratios retain the exact supplied arithmetic.
GROWTH = 0.018
GROSS_MARGIN = 0.1705
SGA_RATIOS = (0.665, 0.655, 0.645, 0.645, 0.645)
DEPRECIATION_RATIO = 82.4 / 3070.4
IMPAIRMENT = 120.0
CAPEX = 250.0
TAX_RATE = 0.255
INVENTORY_DAYS = 2135.8 / (17999.0 - 3071.7) * 365
FLOOR_PLAN_RATIO = 2027.0 / 2135.8
OTHER_WC_RATE = 0.008
MINIMUM_CASH = 25.0
REVOLVER_LIMIT = 850.0
REVOLVER_RATE = 0.06
DEBT_REPAYMENT = 150.0
BUYBACK = 150.0
FLOOR_PLAN_RATE = 0.0467
DEBT_RATE = 0.0544
COST_OF_EQUITY = 0.10
TERMINAL_GROWTH = 0.025
SHARES = 17.951349

# The supplied rounded aggregates imply opening equity of 3,891.7.
OPENING = {
    "revenue": 17999.0,
    "cash": 40.4,
    "inventory": 2135.8,
    "ppe": 3070.4,
    "other_assets": 6371.6,
    "floor_plan": 2027.0,
    "debt": 3572.0,
    "revolver": 0.0,
    "other_liabilities": 2127.5,
    "equity": 3891.7,
}


def assert_balanced(year, balance_gap, cash, revolver):
    if abs(balance_gap) > 1e-7:
        raise AssertionError(f"FY{year}E: assets minus liabilities minus equity = {balance_gap:.1f}")
    if cash < MINIMUM_CASH - 1e-7:
        raise AssertionError(f"FY{year}E: cash below minimum by {MINIMUM_CASH - cash:.1f}")
    if revolver > REVOLVER_LIMIT + 1e-7:
        raise AssertionError(f"FY{year}E: revolver above limit by {revolver - REVOLVER_LIMIT:.1f}")
    if revolver < -1e-7:
        raise AssertionError(f"FY{year}E: revolver is negative by {-revolver:.1f}")


def project():
    prior = OPENING
    rows = []
    for year, sga_ratio in zip(YEARS, SGA_RATIOS):
        # Income statement: all interest uses opening balances.
        revenue = prior["revenue"] * (1 + GROWTH)
        gross_profit = revenue * GROSS_MARGIN
        cost_of_sales = revenue - gross_profit
        sga = gross_profit * sga_ratio
        depreciation = prior["ppe"] * DEPRECIATION_RATIO
        operating_income = gross_profit - sga - depreciation - IMPAIRMENT
        floor_interest = prior["floor_plan"] * FLOOR_PLAN_RATE
        debt_interest = prior["debt"] * DEBT_RATE
        revolver_interest = prior["revolver"] * REVOLVER_RATE
        interest = floor_interest + debt_interest + revolver_interest
        pretax = operating_income - interest
        tax = max(0.0, pretax) * TAX_RATE
        net_income = pretax - tax

        # Balance sheet except cash.
        inventory = cost_of_sales * INVENTORY_DAYS / 365
        floor_plan = inventory * FLOOR_PLAN_RATIO
        ppe = prior["ppe"] + CAPEX - depreciation
        change_other_wc = OTHER_WC_RATE * (revenue - prior["revenue"])
        other_assets = prior["other_assets"] + change_other_wc - IMPAIRMENT
        repayment = min(DEBT_REPAYMENT, prior["debt"])
        debt = prior["debt"] - repayment
        other_liabilities = prior["other_liabilities"]
        equity = prior["equity"] + net_income - BUYBACK

        change_inventory = inventory - prior["inventory"]
        change_floor_plan = floor_plan - prior["floor_plan"]
        operating_cash_flow = (net_income + depreciation + IMPAIRMENT
                               - change_inventory - change_other_wc)
        investing_cash_flow = -CAPEX
        fcfe = operating_cash_flow + investing_cash_flow + change_floor_plan - repayment

        # Revolver is a financing bridge. It is excluded from FCFE and drawn
        # only after the specified cash-before-revolver calculation.
        cash_before_revolver = prior["cash"] + fcfe - BUYBACK
        if cash_before_revolver < MINIMUM_CASH:
            revolver_change = MINIMUM_CASH - cash_before_revolver
        else:
            revolver_change = -min(prior["revolver"], cash_before_revolver - MINIMUM_CASH)
        if revolver_change == 0:
            revolver_change = 0.0
        revolver = prior["revolver"] + revolver_change
        financing_cash_flow = change_floor_plan - repayment - BUYBACK + revolver_change
        cash = prior["cash"] + operating_cash_flow + investing_cash_flow + financing_cash_flow

        assets = cash + inventory + ppe + other_assets
        liabilities = floor_plan + debt + revolver + other_liabilities
        balance_gap = assets - liabilities - equity
        row = {
            "year": year,
            "revenue": revenue,
            "cost_of_sales": cost_of_sales,
            "gross_profit": gross_profit,
            "sga": sga,
            "depreciation": depreciation,
            "impairment": IMPAIRMENT,
            "operating_income": operating_income,
            "floor_interest": floor_interest,
            "debt_interest": debt_interest,
            "revolver_interest": revolver_interest,
            "interest": interest,
            "pretax": pretax,
            "tax": tax,
            "net_income": net_income,
            "cash": cash,
            "inventory": inventory,
            "ppe": ppe,
            "other_assets": other_assets,
            "assets": assets,
            "floor_plan": floor_plan,
            "debt": debt,
            "revolver": revolver,
            "other_liabilities": other_liabilities,
            "liabilities": liabilities,
            "equity": equity,
            "operating_cash_flow": operating_cash_flow,
            "investing_cash_flow": investing_cash_flow,
            "financing_cash_flow": financing_cash_flow,
            "change_inventory": change_inventory,
            "inventory_cash_effect": -change_inventory,
            "change_other_wc": change_other_wc,
            "other_wc_cash_effect": -change_other_wc,
            "change_floor_plan": change_floor_plan,
            "repayment": repayment,
            "repayment_cash_effect": -repayment,
            "buyback": BUYBACK,
            "buyback_cash_effect": -BUYBACK,
            "revolver_change": revolver_change,
            "fcfe": fcfe,
            "balance_gap": balance_gap,
            "cash_headroom": cash - MINIMUM_CASH,
        }
        rows.append(row)
        prior = row
    return rows


def print_statement(title, rows, lines):
    print(f"\n{title}")
    print(f"{'USD millions':<30}" + "".join(f"{row['year']:>12}" for row in rows))
    for label, key in lines:
        print(f"{label:<30}" + "".join(f"{(0.0 if abs(row[key]) < 1e-7 else row[key]):>12.1f}" for row in rows))


def main():
    rows = project()
    print_statement("Income statement", rows, (
        ("Revenue", "revenue"),
        ("Cost of sales", "cost_of_sales"),
        ("Gross profit", "gross_profit"),
        ("SG&A", "sga"),
        ("Depreciation", "depreciation"),
        ("Impairment", "impairment"),
        ("Operating income", "operating_income"),
        ("Floor-plan interest", "floor_interest"),
        ("Term-debt interest", "debt_interest"),
        ("Revolver interest", "revolver_interest"),
        ("Pretax income", "pretax"),
        ("Tax", "tax"),
        ("Net income", "net_income"),
    ))
    print_statement("Balance sheet", rows, (
        ("Cash", "cash"),
        ("Inventory", "inventory"),
        ("PP&E", "ppe"),
        ("Other assets", "other_assets"),
        ("Total assets", "assets"),
        ("Floor plan", "floor_plan"),
        ("Term debt", "debt"),
        ("Revolver", "revolver"),
        ("Other liabilities", "other_liabilities"),
        ("Total liabilities", "liabilities"),
        ("Equity", "equity"),
    ))
    print_statement("Cash flow statement", rows, (
        ("Net income", "net_income"),
        ("Depreciation", "depreciation"),
        ("Impairment", "impairment"),
        ("Inventory cash effect", "inventory_cash_effect"),
        ("Other working capital effect", "other_wc_cash_effect"),
        ("Operating cash flow", "operating_cash_flow"),
        ("Capital spending", "investing_cash_flow"),
        ("Change in floor plan", "change_floor_plan"),
        ("Term-debt repayment", "repayment_cash_effect"),
        ("Share buyback", "buyback_cash_effect"),
        ("Change in revolver", "revolver_change"),
        ("Financing cash flow", "financing_cash_flow"),
        ("FCFE before buybacks", "fcfe"),
        ("Ending cash", "cash"),
    ))
    print_statement("Checks", rows, (
        ("Assets - liabilities - equity", "balance_gap"),
        ("Cash above minimum", "cash_headroom"),
    ))
    for row in rows:
        assert_balanced(row["year"], row["balance_gap"], row["cash"], row["revolver"])

    if COST_OF_EQUITY <= TERMINAL_GROWTH:
        raise ValueError("Cost of equity must exceed terminal growth")
    pv_fcfe = sum(row["fcfe"] / (1 + COST_OF_EQUITY) ** index
                  for index, row in enumerate(rows, 1))
    terminal_fcfe = (rows[-1]["fcfe"] + rows[-1]["repayment"]) * (1 + TERMINAL_GROWTH)
    terminal_value = terminal_fcfe / (COST_OF_EQUITY - TERMINAL_GROWTH)
    pv_terminal = terminal_value / (1 + COST_OF_EQUITY) ** len(rows)
    equity_value = pv_fcfe + pv_terminal
    terminal_share = pv_terminal / equity_value
    print("\nValuation")
    print(f"Equity value (USD millions): {equity_value:,.2f}")
    print(f"Share of value after 2030: {terminal_share:.2%}")
    print(f"Value per share: ${equity_value / SHARES:,.2f}")


if __name__ == "__main__":
    main()
