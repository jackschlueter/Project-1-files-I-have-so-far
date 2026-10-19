# Asbury Comparable P/E Valuation Walkthrough

This is a learning exercise based on the December 31, 2024 case inputs. Its main deliverable is [`asbury_peer_valuation.py`](asbury_peer_valuation.py), a standard-library Python calculator for a comparable-company price-to-earnings (P/E) valuation.

> **Disclaimer:** This material is for educational purposes only. It is not legal, tax, accounting, financial, or investment advice, and it is not a recommendation to buy or sell any security. Consult a qualified professional before making decisions based on it.

It does not fetch data, install packages, or use cash/debt. P/E is an equity multiple:

\[
\text{P/E} = \frac{\text{share price}}{\text{diluted EPS}}
\]

To estimate a target price from a peer multiple:

\[
\text{implied target price} = \text{peer P/E} \times \text{target diluted EPS}
\]

## Why use a comparable P/E?

A share price alone is not comparable across companies because share counts differ. P/E standardizes market price by earnings attributable to each share. It answers: how much is the market paying for one dollar of a company’s earnings?

This is a market-based cross-check to a discounted cash flow (DCF) valuation:

- A DCF estimates value from explicit forecasts of cash flows, growth, and risk.
- A comparable P/E applies how the market prices similar earnings.
- The two approaches should be compared, not blindly averaged.

A lower P/E does not automatically mean a better investment. It can reflect slower expected growth, greater risk, more leverage, weaker margins, or temporarily elevated earnings. P/E is not meaningful for negative EPS or for earnings distorted by large nonrecurring items.

## Business-based peer selection

The target is **Asbury Automotive Group (ABG)**. It earns from franchised new- and used-vehicle sales, parts/service and collision work, and finance-and-insurance (F&I) products. Its Total Care Auto business also provides F&I products.

Peer selection was decided from business economics before looking at price:

| Company | Decision | Business rationale | Key qualification |
|---|---|---|---|
| AutoNation (AN) | Use | U.S. franchised dealer model with new/used vehicle sales, after-sales service, collision, and F&I earnings. | Its used-car, auction, mobile-repair, and auto-finance activities create a different business mix and potential credit exposure. |
| Group 1 Automotive (GPI) | Qualify | Same core dealer, service, parts, and finance/insurance operating model. | Meaningful non-U.S. exposure and a differing brand/geographic mix make it a qualified, rather than unqualified, peer. |

An industry label alone is insufficient. Earnings comparability requires similar business mix, growth, risk, and accounting/earnings definitions. The case keeps GPI as a qualified peer; a mathematical sensitivity result does not by itself change that business judgment.

## Case inputs

The file begins with editable `TARGET` and `PEERS` dictionaries:

| Company / role | Dec. 31, 2024 closing price | FY2024 total GAAP diluted EPS |
|---|---:|---:|
| ABG, target | $243.03 | $21.50 |
| AN, peer | $169.84 | $16.92 |
| GPI, qualified peer | $421.48 | $36.81 |

The retrospective training case pairs year-end prices with subsequently reported annual earnings. ABG is the target and is never allowed to enter its own peer set.

## The Python calculator

`asbury_peer_valuation.py` is deliberately simple and editable:

1. Edit the target and peer values at the top of the file.
2. It identifies a company by ticker (falling back to name), removes duplicate peers, and excludes the target.
3. It computes each valid peer’s P/E as `price / diluted_eps`.
4. It calculates the minimum, median, and maximum usable peer P/E.
5. It multiplies each of those unrounded multiples by target EPS to produce an implied ABG price range.
6. It performs leave-one-out sensitivity: remove each peer, recompute the remaining median-implied price, and compare it with the full-peer median estimate.

The calculator retains full precision in calculations. It only formats displayed P/E multiples to six decimal places and dollar values to cents.

### Handling unusable inputs

Missing, nonnumeric, or nonpositive prices and diluted EPS are labeled **not meaningful**. A peer with invalid inputs is not used in the median.

- No usable peers: no implied-price estimate is available.
- One usable peer: it is shown as a **reference estimate**, not a range.
- Invalid target EPS: all implied target-price calculations are not meaningful.

P/E values are never adjusted with cash or debt; doing so would incorrectly mix an equity multiple with enterprise-value concepts.

## Run the file

From `/Users/jakes/Documents/Courses`, run:

```bash
python3 'AIFinance2026/Jack Schlueter/asbury_peer_valuation.py'
```

## Case calculation and validation

\[
\text{AN P/E} = \frac{169.84}{16.92} = 10.037825\times
\]

\[
\text{GPI P/E} = \frac{421.48}{36.81} = 11.450149\times
\]

| Check | Result |
|---|---:|
| AN P/E | 10.037825× |
| GPI P/E | 11.450149× |
| Median peer P/E | 10.743987× |
| ABG implied range | $215.81–$246.18 |
| ABG at peer median | $231.00 |

The implied range comes from applying the low and high peer multiples to ABG’s $21.50 EPS. The median-implied price is based on the unrounded median P/E.

## Leave-one-out interpretation

GPI has the higher P/E. Therefore, removing GPI should lower the remaining-peer valuation.

The calculator confirms this:

| Removal | Remaining estimate | Change from two-peer median estimate |
|---|---:|---:|
| Remove AN | $246.18 | +$15.18 |
| Remove GPI | $215.81 | −$15.18 |

Removing GPI leaves AN’s 10.037825× multiple as the only input. With one peer, the minimum, median, and maximum are identical; there is no observed peer dispersion. That is why the result is a reference estimate rather than a range.

## Practical checklist

- Keep target and peer inputs on the same EPS basis: trailing or forward, GAAP or consistently normalized, and diluted.
- Decide use, qualify, or exclude from business evidence before reviewing prices.
- Investigate unusual gains, impairments, acquisition effects, and materially different growth/risk profiles before treating a P/E as comparable.
- Retain unrounded values until final display.
- Treat the result as a relative-valuation cross-check, not an automatic investment conclusion.
