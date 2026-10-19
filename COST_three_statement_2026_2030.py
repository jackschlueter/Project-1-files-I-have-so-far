"""Costco classroom three-statement forecast and FCFE valuation.

USD millions except per-share values. Forecasts are judgments, not Costco
guidance. This classroom model is for educational use only and is not
investment advice. The opening balance sheet is the FY2025 10-K, Item 8. Run with:

    python3 COST_three_statement_2026_2030.py

Sources:
FY2025 10-K: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm
FY2024 10-K: https://www.sec.gov/Archives/edgar/data/909832/000090983224000049/cost-20240901.htm
FY2023 10-K: https://www.sec.gov/Archives/edgar/data/909832/000090983223000042/cost-20230903.htm
FY2026 Q3 10-Q (share count): https://www.sec.gov/Archives/edgar/data/909832/000090983226000051/cost-20260510.htm
"""

YEARS = range(2026, 2031)

# FY2025 reported amounts. The $75m current debt portion is disclosed in
# Note 4 and included in reported other current liabilities. Reclassifying it
# leaves total liabilities unchanged; it is not a new liability or a plug.
OPENING = {
    "sales": 269_912.0,
    "fees": 5_323.0,
    "paid_members": 81.0,  # Millions of paid memberships at FY2025 year-end.
    "cash": 14_161.0,
    "short_investments": 1_123.0,
    "receivables": 3_203.0,
    "inventory": 18_116.0,
    "other_current_assets": 1_777.0,
    "ppe": 31_909.0,
    "rou_assets": 2_725.0,
    "other_long_assets": 4_085.0,
    "accounts_payable": 19_783.0,
    "accrued_payroll": 5_205.0,
    "member_rewards": 2_677.0,
    "deferred_fees": 2_854.0,
    "other_current_liabilities": 6_589.0 - 75.0,
    "debt": 5_713.0 + 75.0,
    "lease_liabilities": 2_460.0,
    "other_long_liabilities": 2_654.0,
    "equity": 29_164.0,
}

# Prior discussion's FY2026-2030 assumption set. All are judgments.
SALES_GROWTH = 0.06            # Near FY2025 comparable growth; below 8.13% reported growth.
BASE_PAID_MEMBER_GROWTH = 0.063  # Rounded FY2025 versus FY2024 paid-member growth.
PAID_MEMBER_GROWTH = BASE_PAID_MEMBER_GROWTH  # Scenario input; annual FY2026-2030 rate.
OPENING_WAREHOUSE_SQFT_PER_STORE = 147_000.0  # FY2025 10-K: approximate average warehouse space.
WAREHOUSE_SQFT_PER_STORE = 147_000.0  # Judgmental FY2026-2030 fleet average; scenario input.
FEE_GROWTH = 0.07              # Member growth/upgrades; no repeated fee hikes assumed.
MERCHANDISE_GROSS_MARGIN = 0.111  # Near FY2025's 11.12%.
SGA_TO_GROSS_PROFIT = 0.71     # Near FY2025's 70.63%; includes depreciation.
INVENTORY_DAYS = 28.0         # Near FY2025 average inventory days.
DEPRECIATION_TO_PPE = 0.076   # Near FY2025 D&A / ending net PP&E.
CAPEX_TO_SALES = 0.02         # Near FY2025 additions to PP&E / net sales.
TAX_RATE = 0.25              # Near the FY2023-2025 effective tax rates.

# Further explicit modeling judgments, with filing anchors where available.
RECEIVABLES_TO_SALES = OPENING["receivables"] / OPENING["sales"]
OTHER_CURRENT_ASSETS_TO_SALES = OPENING["other_current_assets"] / OPENING["sales"]
ACCOUNTS_PAYABLE_TO_MERCH_COST = OPENING["accounts_payable"] / 239_886.0
ACCRUED_PAYROLL_TO_SALES = OPENING["accrued_payroll"] / OPENING["sales"]
MEMBER_REWARDS_TO_SALES = OPENING["member_rewards"] / OPENING["sales"]
DEFERRED_FEES_TO_FEES = OPENING["deferred_fees"] / OPENING["fees"]
OTHER_CURRENT_LIABS_TO_SALES = OPENING["other_current_liabilities"] / OPENING["sales"]
SBC_TO_SALES = 860.0 / OPENING["sales"]  # FY2025 cash flow statement.
INTEREST_TO_DEBT = 154.0 / OPENING["debt"]  # FY2025 expense / net debt carrying value.
DEBT_REPAYMENTS = {2026: 75.0, 2027: 2_250.0, 2028: 0.0,
                   2029: 148.0, 2030: 1_750.0}  # FY2025 10-K, Note 4.
MINIMUM_CASH = 10_000.0      # Judgment: roughly FY2024 year-end cash.
COST_OF_EQUITY = 0.10        # Judgmental classroom discount rate.
TERMINAL_GROWTH = 0.025      # Judgment; below cost of equity.
SHARES_MILLIONS = 443.514    # May 10, 2026 Form 10-Q, shares outstanding.

# Constant items are held flat because this simple model has no defensible
# lease, short-investment, or long-term-asset acquisition schedule.
CONSTANT_ITEMS = ("short_investments", "rou_assets", "other_long_assets",
                  "lease_liabilities", "other_long_liabilities")
ASSET_KEYS = ("cash", "short_investments", "receivables", "inventory",
              "other_current_assets", "ppe", "rou_assets", "other_long_assets")
LIABILITY_KEYS = ("accounts_payable", "accrued_payroll", "member_rewards",
                  "deferred_fees", "other_current_liabilities", "debt",
                  "lease_liabilities", "other_long_liabilities")
OPERATING_ASSET_KEYS = ("receivables", "inventory", "other_current_assets")
OPERATING_LIABILITY_KEYS = ("accounts_payable", "accrued_payroll",
                            "member_rewards", "deferred_fees",
                            "other_current_liabilities")
TOLERANCE = 1e-7


def totals(row):
    return (sum(row[key] for key in ASSET_KEYS),
            sum(row[key] for key in LIABILITY_KEYS))


def require_close(year, name, gap):
    if abs(gap) > TOLERANCE:
        raise AssertionError(f"FY{year}: {name} gap = {gap:,.2f} million")


def forecast():
    opening_assets, opening_liabilities = totals(OPENING)
    require_close(2025, "opening assets - liabilities - equity",
                  opening_assets - opening_liabilities - OPENING["equity"])
    require_close(2025, "opening assets versus filing", opening_assets - 77_099.0)
    require_close(2025, "opening liabilities versus filing", opening_liabilities - 47_935.0)

    prior = OPENING
    rows = []
    for year in YEARS:
        # Base sales/fee growth already embeds historical member growth. A
        # member-growth scenario changes both amounts relative to that base,
        # assuming constant spend and fee yield per member versus the base.
        member_factor = (1 + PAID_MEMBER_GROWTH) / (1 + BASE_PAID_MEMBER_GROWTH)
        paid_members = prior["paid_members"] * (1 + PAID_MEMBER_GROWTH)
        sales = prior["sales"] * (1 + SALES_GROWTH) * member_factor
        if year == 2026:
            # Apply a changed fleet-average footprint once to the sales level;
            # later years compound at SALES_GROWTH. Constant sales per square
            # foot is a scenario judgment, not a disclosed company forecast.
            sales *= WAREHOUSE_SQFT_PER_STORE / OPENING_WAREHOUSE_SQFT_PER_STORE
        fees = prior["fees"] * (1 + FEE_GROWTH) * member_factor
        revenue = sales + fees
        merchandise_cost = sales * (1 - MERCHANDISE_GROSS_MARGIN)
        gross_profit = revenue - merchandise_cost
        sga = gross_profit * SGA_TO_GROSS_PROFIT
        ebit = gross_profit - sga  # D&A is already embedded in Costco's SG&A/merchandise costs.
        repayment = DEBT_REPAYMENTS[year]
        if repayment > prior["debt"] + TOLERANCE:
            raise AssertionError(f"FY{year}: scheduled debt repayment exceeds opening debt")
        debt = prior["debt"] - repayment
        interest = (prior["debt"] + debt) / 2 * INTEREST_TO_DEBT
        pretax = ebit - interest
        tax = max(0.0, pretax) * TAX_RATE  # No tax-loss benefit assumed.
        net_income = pretax - tax

        depreciation = prior["ppe"] * DEPRECIATION_TO_PPE
        capex = sales * CAPEX_TO_SALES
        sbc = sales * SBC_TO_SALES
        maintenance_buyback = sbc  # Judgment: cash offset for share compensation.

        row = {
            "year": year, "paid_members": paid_members,
            "sales": sales, "fees": fees, "revenue": revenue,
            "merchandise_cost": merchandise_cost, "gross_profit": gross_profit,
            "sga": sga, "ebit": ebit, "interest": interest, "pretax": pretax,
            "tax": tax, "net_income": net_income, "depreciation": depreciation,
            "capex": capex, "sbc": sbc, "maintenance_buyback": maintenance_buyback,
            "receivables": sales * RECEIVABLES_TO_SALES,
            "inventory": merchandise_cost * INVENTORY_DAYS / 365,
            "other_current_assets": sales * OTHER_CURRENT_ASSETS_TO_SALES,
            "ppe": prior["ppe"] + capex - depreciation,
            "accounts_payable": merchandise_cost * ACCOUNTS_PAYABLE_TO_MERCH_COST,
            "accrued_payroll": sales * ACCRUED_PAYROLL_TO_SALES,
            "member_rewards": sales * MEMBER_REWARDS_TO_SALES,
            "deferred_fees": fees * DEFERRED_FEES_TO_FEES,
            "other_current_liabilities": sales * OTHER_CURRENT_LIABS_TO_SALES,
            "debt": debt,
        }
        for key in CONSTANT_ITEMS:
            row[key] = prior[key]

        increase_op_assets = sum(row[key] - prior[key] for key in OPERATING_ASSET_KEYS)
        increase_op_liabilities = sum(row[key] - prior[key] for key in OPERATING_LIABILITY_KEYS)
        cfo = (net_income + depreciation + sbc - increase_op_assets
               + increase_op_liabilities)
        cfi = -capex
        cff = -repayment - maintenance_buyback
        row["cfo"], row["cfi"], row["cff"] = cfo, cfi, cff
        row["cash"] = prior["cash"] + cfo + cfi + cff
        row["equity"] = prior["equity"] + net_income + sbc - maintenance_buyback
        row["repayment"] = repayment
        # Buybacks offsetting SBC are treated as a required cash cost of
        # keeping current shares whole; other discretionary buybacks are zero.
        row["fcfe"] = cfo + cfi - repayment - maintenance_buyback
        row["assets"], row["liabilities"] = totals(row)
        row["balance_gap"] = row["assets"] - row["liabilities"] - row["equity"]
        row["cash_gap"] = row["cash"] - (prior["cash"] + cfo + cfi + cff)
        row["ppe_gap"] = row["ppe"] - (prior["ppe"] + capex - depreciation)
        row["debt_gap"] = row["debt"] - (prior["debt"] - repayment)
        row["equity_gap"] = row["equity"] - (prior["equity"] + net_income + sbc - maintenance_buyback)
        row["minimum_cash_headroom"] = row["cash"] - MINIMUM_CASH
        rows.append(row)
        prior = row
    return rows


def check(rows):
    for row in rows:
        year = row["year"]
        for name in ("balance_gap", "cash_gap", "ppe_gap", "debt_gap", "equity_gap"):
            require_close(year, name, row[name])
        if row["minimum_cash_headroom"] < -TOLERANCE:
            raise AssertionError(
                f"FY{year}: cash below minimum by {-row['minimum_cash_headroom']:,.2f} million"
            )
        if row["fcfe"] < 0:
            print(f"FY{year}: negative FCFE {row['fcfe']:,.1f} million")


def value_equity(rows):
    check(rows)
    if TERMINAL_GROWTH >= COST_OF_EQUITY:
        raise ValueError("Terminal growth must be below cost of equity")
    # The scheduled $1.75bn FY2030 debt repayment is not repeated forever.
    terminal_fcfe = rows[-1]["fcfe"] + rows[-1]["repayment"]
    if terminal_fcfe <= 0:
        raise ValueError("Terminal FCFE is not positive; a Gordon terminal value is undefined here")
    positive_explicit_fcfe = sum(
        max(0.0, row["fcfe"]) / (1 + COST_OF_EQUITY) ** index
        for index, row in enumerate(rows, 1)
    )
    terminal_value = terminal_fcfe * (1 + TERMINAL_GROWTH) / (COST_OF_EQUITY - TERMINAL_GROWTH)
    pv_terminal = terminal_value / (1 + COST_OF_EQUITY) ** len(rows)
    opening_nonoperating_cash = max(0.0, OPENING["cash"] - MINIMUM_CASH)
    opening_short_investments = OPENING["short_investments"]
    equity_value = (positive_explicit_fcfe + pv_terminal
                    + opening_nonoperating_cash + opening_short_investments)
    return positive_explicit_fcfe, pv_terminal, opening_nonoperating_cash, opening_short_investments, equity_value


def print_statement(title, rows, fields):
    print(f"\n{title}")
    print(f"{'USD millions':<32}" + "".join(f"{row['year']:>13}" for row in rows))
    for label, key in fields:
        print(f"{label:<32}" + "".join(f"{row[key]:>13,.1f}" for row in rows))


def main():
    rows = forecast()
    print("COST classroom forecast | USD millions except per share")
    print("Opening: FY2025 Form 10-K; shares: May 2026 Form 10-Q")
    print("Opening assets 77,099; liabilities 47,935; equity 29,164")
    print_statement("Income statement", rows, (
        ("Net sales", "sales"), ("Membership fees", "fees"),
        ("Total revenue", "revenue"), ("Merchandise costs", "merchandise_cost"),
        ("Gross profit", "gross_profit"), ("SG&A", "sga"),
        ("Operating income", "ebit"), ("Interest expense", "interest"),
        ("Pretax income", "pretax"), ("Tax", "tax"),
        ("Net income", "net_income"),
    ))
    print_statement("Operating driver", rows, (("Paid members (millions)", "paid_members"),))
    print_statement("Balance sheet", rows, (
        ("Cash", "cash"), ("Short investments", "short_investments"),
        ("Receivables", "receivables"), ("Inventory", "inventory"),
        ("Other current assets", "other_current_assets"), ("PP&E, net", "ppe"),
        ("ROU assets", "rou_assets"), ("Other long assets", "other_long_assets"),
        ("Total assets", "assets"), ("Accounts payable", "accounts_payable"),
        ("Accrued payroll", "accrued_payroll"), ("Member rewards", "member_rewards"),
        ("Deferred membership fees", "deferred_fees"),
        ("Other current liabilities", "other_current_liabilities"),
        ("Debt, net carrying amount", "debt"),
        ("Lease liabilities", "lease_liabilities"),
        ("Other long liabilities", "other_long_liabilities"),
        ("Total liabilities", "liabilities"), ("Equity", "equity"),
    ))
    print_statement("Cash flow and FCFE", rows, (
        ("Operating cash flow", "cfo"), ("Capital spending", "cfi"),
        ("Debt repayment and buyback", "cff"), ("Ending cash", "cash"),
        ("FCFE after SBC-offset buyback", "fcfe"),
    ))
    print_statement("Checks", rows, (
        ("Assets - liabilities - equity", "balance_gap"),
        ("Cash roll-forward gap", "cash_gap"),
        ("PP&E roll-forward gap", "ppe_gap"),
        ("Debt roll-forward gap", "debt_gap"),
        ("Equity roll-forward gap", "equity_gap"),
        ("Cash above $10bn minimum", "minimum_cash_headroom"),
    ))
    explicit, terminal, cash, investments, equity_value = value_equity(rows)
    print("\nValuation")
    print(f"PV positive FY2026-2030 FCFE: {explicit:,.1f}")
    print(f"PV terminal FCFE: {terminal:,.1f}")
    print(f"Opening excess cash + investments: {cash + investments:,.1f}")
    print(f"Equity value: {equity_value:,.1f}")
    print(f"Value per share ({SHARES_MILLIONS:.3f}m shares): ${equity_value / SHARES_MILLIONS:,.2f}")
    print(f"Terminal share of equity value: {terminal / equity_value:.1%}")
    print("All checks passed")


if __name__ == "__main__":
    main()
