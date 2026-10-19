# Valuation conversation and Lab 07 submission record

This is a consolidated record of the substantive work completed in this chat. It is not a verbatim platform transcript; it preserves the decisions, calculations, sources, limitations, and deliverables needed to review or submit the work.

> **Educational disclaimer:** This document is prepared solely for an academic learning exercise. It is not investment, financial, legal, tax, or accounting advice; it is not a recommendation, solicitation, or offer to buy, sell, or hold any security. The calculations use limited historical inputs and stated assumptions, may contain errors or omissions, and should not be relied on for investment decisions. Consult a qualified professional before making any financial decision.

## File links

### GitHub links — unresolved

No Git repository or configured GitHub remote exists in the current workspace, so genuine GitHub URLs cannot be supplied without fabricating them. Publish the files below to a repository, then replace this section with their GitHub `blob` links.

Expected paths to publish:

- `AIFinance2026/Jack Schlueter/Costco_Peer_Policy_and_Candidate_Log.md`
- `AIFinance2026/Jack Schlueter/costco_peer_valuation.py`
- `AIFinance2026/Jack Schlueter/Costco_DCF.md`
- `AIFinance2026/Jack Schlueter/dcf.py`
- `AIFinance2026/Jack Schlueter/COST-research/Costco_2026-09-03_report.md`
- `AIFinance2026/Jack Schlueter/COST-research/sources.md`
- `AIFinance2026/Jack Schlueter/asbury_peer_valuation.py`
- `AIFinance2026/Jack Schlueter/asbury_peer_valuation_walkthrough.md`

### Workspace deliverables

- [Costco peer policy, sources, validation, DCF comparison, and submission narrative](Costco_Peer_Policy_and_Candidate_Log.md)
- [Costco Lab 07 peer-P/E calculator](costco_peer_valuation.py)
- [Saved Week 3 DCF](Costco_DCF.md) and [DCF calculator](dcf.py)
- [Week 3 Costco report](COST-research/Costco_2026-09-03_report.md) and [running source register](COST-research/sources.md)
- [Asbury P/E calculator](asbury_peer_valuation.py) and [Asbury walkthrough](asbury_peer_valuation_walkthrough.md)

## Conversation record

### 1. Earlier Asbury practice case — retained separately

The saved Asbury calculator was run successfully. It used ABG as the target, AutoNation (AN) and Group 1 Automotive (GPI) as the two peers, and FY2024 GAAP diluted EPS. Its result was an ABG peer-P/E range of **$215.81–$246.18**, with a median-implied estimate of **$231.00**. That case is a method exercise only; none of its prices, EPS inputs, or results were used in the Costco calculation.

### 2. Costco target, date, and initial policy

- **Target:** Costco Wholesale Corporation (COST).
- **Week 3 comparison date:** August 31, 2026.
- **Costco annual earnings basis:** FY2025 reported GAAP diluted EPS of **$18.21**, fiscal year ended August 31, 2025; Costco's reported EPS is positive, so P/E is meaningful. [Costco FY2025 Form 10-K, Item 8](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm)

The policy was stated before calculating multiples: a usable peer must be a publicly traded parent whose principal economics are recurring membership-warehouse retail—meaningful membership income, large-format low-price/high-volume club retail across grocery/consumables and general merchandise, a material physical-club plus omnichannel operation, and positive annual reported GAAP diluted EPS public by the valuation date. Geography, club scale, gasoline, merchandise mix, membership economics, renewal, e-commerce, capital intensity, leverage, and growth are qualifications. A candidate is excluded if the public parent’s multiple mainly values another business model or its annual EPS is not comparable.

The policy may not be changed after viewing results. Any revision requires new evidence and an explanation before recalculation.

### 3. Candidate decisions from opened sources

| Candidate | Decision | Evidence and reasoning | Reported annual diluted EPS public by Aug. 31, 2026 |
|---|---|---|---:|
| BJ’s Wholesale Club Holdings (BJ) | **Use, subject to review** | BJ's is a membership-warehouse operator offering groceries, fresh foods, general merchandise, gasoline, ancillary services, and digital fulfillment. Its eastern-U.S. concentration, 263-club scale, gasoline exposure, and coupon/promotional approach qualify the multiple. [BJ 10-K, Item 1—Business](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/bj-20260131.htm); [BJ annual earnings release, Mar. 5, 2026](https://investors.bjs.com/press-releases/press-release-details/2026/BJs-Wholesale-Club-Holdings-Inc--Announces-Fourth-Quarter-and-Full-Fiscal-2025-Results/default.aspx) | $4.38; fiscal 2025, 52 weeks ended Jan. 31, 2026; announced Mar. 5, 2026 |
| Walmart / Sam’s Club (WMT) | **Exclude** | Sam’s Club is a membership-only warehouse segment, but WMT’s public EPS reflects Walmart U.S., international, e-commerce, and other operations. Sam’s Club represented 13% of FY2026 consolidated sales, and Walmart does not disclose stand-alone Sam’s Club net income or EPS. WMT’s P/E does not value a comparable stand-alone club business. [Walmart 10-K, Item 1—Sam’s Club U.S. Segment](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm); [FY2026 results](https://corporate.walmart.com/news/events/fy2026-q4-earnings-release) | $2.73 WMT consolidated FY2026 GAAP diluted EPS, year ended Jan. 31, 2026; released Feb. 19, 2026. Recorded only to support exclusion; not used in P/E. |

Evidence that would cause BJ’s rejection: loss of a principally membership-warehouse model; material EPS distortion from gasoline, promotions, mix, or nonrecurring items without a consistent treatment for Costco; risk/growth/capital differences that prevent the multiple from serving as a reasonable reference; or failure to pair the dated price with a compatible annual GAAP diluted EPS basis. Walmart/Sam’s would remain excluded unless a separately traded Sam’s Club security or reliable stand-alone EPS becomes available.

### 4. Price and earnings input record

| Company / role | Aug. 31, 2026 close | Price evidence | Reported annual GAAP diluted EPS | Fiscal year-end | Publication date | Earnings locator |
|---|---:|---|---:|---|---|---|
| Costco / target | $943.89 | [StockAnalysis COST historical-price row](https://stockanalysis.com/stocks/cost/history/) | $18.21 | Aug. 31, 2025 | Oct. 8, 2025 | [Costco FY2025 Form 10-K, Item 8, p. 34](https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm) |
| BJ’s / use peer | $90.65 | [StockAnalysis BJ historical-price row](https://stockanalysis.com/stocks/bj/history/) | $4.38 | Jan. 31, 2026 | Mar. 5, 2026 | [BJ FY2025 Form 10-K, statements of operations / EPS](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/bj-20260131.htm); [annual release](https://investors.bjs.com/press-releases/press-release-details/2026/BJs-Wholesale-Club-Holdings-Inc--Announces-Fourth-Quarter-and-Full-Fiscal-2025-Results/default.aspx) |

All inputs are U.S. dollars per share, annual, reported GAAP diluted EPS public by the valuation date. Adjusted EPS and quarterly results were not used. BJ separately reported adjusted FY2025 EPS of $4.40, which was retained separately and excluded from the calculation.

Nasdaq historical pages were checked first but did not return the dated data during this session. The Nasdaq verification is therefore unresolved; named historical-price sources are recorded above rather than treating missing Nasdaq data as verified.

### 5. Validation and checked peer result

Only Costco and BJ (the use peer) were entered in the Costco Lab 07 calculator. Walmart/Sam’s was deliberately omitted because it is excluded—not because its multiple would be inconvenient.

Manual arithmetic check:

\[
\text{BJ P/E} = \frac{\$90.65}{\$4.38} = 20.696347\times
\]

\[
\text{Costco reference price} = 20.696347\times\$18.21 = \$376.88
\]

The prediction before changing the peer set was that removing BJ would leave no estimate, because it is the only usable peer. The calculator confirmed: **`Remove BJ: no estimate (no usable peers remain)`**. Therefore $376.88 is a **single-peer reference estimate**, not a defendable range. A range is withheld rather than invented.

Run command:

```bash
python3 'AIFinance2026/Jack Schlueter/costco_peer_valuation.py'
```

### 6. DCF comparison

| Method | Result and date | Main assumption or limitation |
|---|---|---|
| Week 3 DCF | **$263.20–$434.39** per diluted share across the saved 9%–11% WACC and 2%–4% terminal-growth sensitivity grid; base case **$324.54**. FY2025 inputs, fiscal year ended Aug. 31, 2025. Saved market-price comparison: $902.75 on Sept. 9, 2026. | Five-year FCFF growth is a 6.5583% historical sales-CAGR assumption; WACC is a 10% unresolved placeholder; terminal value is 73.4% of enterprise value. [Saved DCF](Costco_DCF.md) |
| Peer P/E | **$376.88 single-peer reference** on Aug. 31, 2026. | One approved peer; annual reported GAAP diluted EPS for both companies, but different fiscal year-ends. |

The peer comparison adds a market-based earnings cross-check to a cash-flow valuation. Its reference estimate falls within the saved DCF sensitivity range but above the DCF base case. The methods are not averaged: DCF discounts forecast FCFF, then converts enterprise value to equity value per share; peer P/E applies an equity multiple to Costco EPS. Both output Costco equity value per share, so they can be compared, but they reflect different assumptions.

### 7. Skeptical review and judgment

The weakest supported DCF assumption is the **10% WACC**. The saved DCF says it is a placeholder because Costco’s 10-K does not give the market cost of equity. This matters especially because terminal value is 73.4% of enterprise value.

| Skeptical criticism | Judgment | Evidence-based reason |
|---|---|---|
| WACC is the weakest supported assumption. | **Accept** | The saved DCF calls it unresolved. |
| The displayed DCF and P/E market-price comparisons use different dates. | **Accept** | DCF uses Sept. 9, 2026; P/E uses Aug. 31, 2026. |
| DCF and P/E value incompatible objects and cannot be compared. | **Reject** | DCF converts enterprise value to equity value per share; P/E is already equity per share. Cross-checking is valid; averaging is not. |
| Annual GAAP diluted EPS bases are fully comparable. | **Unresolved** | Accounting basis and currency align, but Costco and BJ fiscal year-ends differ by seven months. |

The question most likely to change the decision is: **What primary-source or market-data evidence supports a defensible Costco WACC and normalized FCFF growth path that raises the DCF enough to create a margin of safety at the Aug. 31, 2026 price?** No current source supplies that evidence, so the answer is not assumed.

### 8. Conditional investment call

**Watch / defer; do not initiate now.** The defendable DCF sensitivity range is $263.20–$434.39, and the distinct peer-P/E result is a $376.88 BJ single-peer reference. Both sit materially below the recorded market prices. I withhold a peer range because only one candidate meets the policy.

The decision could change if primary or market evidence supports a defensible WACC and normalized FCFF forecast that materially improves the DCF under disclosed assumptions. A second candidate satisfying the unchanged membership-warehouse policy, with same-date price and compatible annual reported GAAP diluted EPS, would improve the peer cross-check but would not automatically change the decision.

## Merit-anchor self-audit

| Criterion | Evidence in this record | Self-assessment |
|---|---|---:|
| Problem / decision | Target, date, and peer policy precede selection. | 5 / 5 |
| Data / evidence | Two candidate decisions link to opened primary sources; prices and annual GAAP-diluted EPS bases are traced. Nasdaq historical-date verification remains explicitly unresolved. | 4 / 5 |
| Validation | BJ division was checked manually; calculator result and removal-of-sole-peer consequence were predicted, run, and interpreted. | 5 / 5 |
| Financial judgment | DCF range and peer reference are kept separate; limitations and conditional watch/defer action are explained. | 5 / 5 |
| Explanation / transfer | The method’s causal distinction and AI-criticism judgments are sourced and owned. | 5 / 5 |

The only scored weakness is the unavailable Nasdaq dated-price verification. It is recorded once rather than counted again across criteria.
