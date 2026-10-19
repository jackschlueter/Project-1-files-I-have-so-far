# Meridian Foundation Reserve: mandate check

Case: fictional $100 million reserve. Percentages below are percentages of total assets.

## Sort the CIO's statements

| ID | Category | One-line reason |
|---|---|---|
| S1 | Hard constraint | The seven-year horizon frames the mandate, and annual rebalancing sets a required schedule. |
| S2 | Objective | CPI + 4% net of costs over rolling five-year periods is the stated return goal, not a guaranteed result. |
| S3 | Hard constraint | Four quarterly payouts require $3 million (3% of assets) in cash or daily-liquid government securities. |
| S4 | Objective | The 60/40 mix is a performance benchmark; it does not require the holdings to match those weights. |
| S5 | Hard constraint | Borrowing, short sales, and derivatives are prohibited. |
| S6 | Hard constraint | Combined securities of any non-exempt issuer cannot exceed 8% of the portfolio. |
| S7 | Hard constraint | Annual turnover above 25% requires committee approval. |
| S8 | Hard constraint | At least 90% of assets must be redeemable within five business days. |
| S9 | Unverifiable promise | A calendar-year loss ceiling has no specified risk measure or breach procedure and cannot be guaranteed from holdings. |
| S10 | Missing | The CIO has not specified what the pilot should optimize; the listed sector, ESG, tax, and home-bias preferences are absent. |

S1 and S4 mix different kinds of information. For a machine-readable policy, split S1 into `horizon_years = 7` and `rebalance_frequency = annual`; record S4 as `benchmark = 60% global equities / 40% U.S. investment-grade bonds`, not as an allocation limit.

## Candidate checks

Reserve-eligible holdings are cash, Treasury bills, and the 10-year Treasury note. Cash, Treasuries, and diversified funds are exempt from the single-issuer cap; Acme stock and bonds count together.

| Check | Rule | A | B | C |
|---|---:|---:|---:|---:|
| Holdings sum | 100% | 100% | 100% | 100% |
| Reserve-eligible assets | At least 3% | 14% = $14m; pass | 1% = $1m; fail | 2% = $2m; fail |
| Redeemable within five business days | At least 90% | 100%; pass | 85%; fail | 100%; pass |
| Acme combined issuer exposure | At most 8% | 0%; pass | 9%; fail | 8%; pass |
| Long-only holdings | Required | Pass on listed positions | Pass on listed positions | Pass on listed positions |

**Result:** A is the only candidate that passes every hard limit testable from the supplied holdings. B fails the reserve, liquidity, and issuer tests. C fails the reserve test. The benchmark does not disqualify any candidate by itself.

This is a holdings-based eligibility check, not final permission to implement A. The snapshot does not establish annual turnover, whether rebalancing will occur, or whether any borrowing, shorts, or derivatives exist outside the listed holdings. The CPI + 4% objective cannot be certified from weights alone.

## CIO decisions before optimization

1. Specify the pilot's objective function (for example, expected net real return, tracking error to the 60/40 benchmark, or another measure), its measurement period, and which constraints take priority if objectives conflict. The 60/40 benchmark alone does not answer this.
2. Replace S9's absolute loss promise with an operational risk rule: define the loss measure and observation dates, whether it is a hard limit or a risk target, the model/scenarios or confidence level if relevant, who monitors it, and what happens on breach. An absolute calendar-year loss cap cannot be guaranteed for a long-only market portfolio.
3. Specify whether the $3 million reserve floor is maintained continuously or tested at set dates, and how payouts and replenishment work. The supplied holding table expressly counts the 10-year Treasury note as reserve-eligible.
4. Supply starting holdings or trades and the turnover calculation, and identify the approval record for any turnover above 25%. Confirm the annual rebalancing procedure and authority.

## Sceptical colleague's check

- A's reserve is 2% cash + 2% Treasury bills + 10% Treasury note = 14%.
- B's 15% real estate fund takes five-day liquidity to 85%, and its 5% Acme bonds plus 4% Acme stock breach the 8% issuer cap.
- C's 1% cash + 1% Treasury bills leave a $1 million reserve shortfall even though its other tested limits pass.
- A portfolio matching the benchmark or aiming at CPI + 4% is not automatically compliant; eligibility requires passing each hard rule.

Reference: CFA Institute, [*Elements of an Investment Policy Statement for Institutional Investors*](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-institutional-investors.pdf) (2010). The paper recommends documenting objectives, constraints, liquidity, governance, risk measures, and rebalancing procedures. Its illustrative figures are not facts about Meridian.
