"""Costco P/E comparable-company valuation — Lab 07 inputs.

All inputs are U.S. dollars per share.  Use annual, reported GAAP diluted EPS
that was publicly available by the August 31, 2026 valuation date.
"""

from statistics import median


TARGET = {
    "ticker": "COST",
    "name": "Costco Wholesale Corporation",
    "price": 943.89,
    "diluted_eps": 18.21,
}

# Only candidates marked use or qualify in Costco_Peer_Policy_and_Candidate_Log.md
# belong here. Walmart/Sam's Club is excluded and intentionally omitted.
PEERS = [
    {
        "ticker": "BJ",
        "name": "BJ's Wholesale Club Holdings, Inc.",
        "price": 90.65,
        "diluted_eps": 4.38,
    },
]


def valid_positive(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def main():
    target_eps = TARGET["diluted_eps"]
    if not valid_positive(target_eps):
        print("Target annual reported diluted EPS is missing, zero, or negative; P/E is not meaningful.")
        return

    print("Costco P/E Comparable-Company Valuation — Lab 07")
    print("=" * 51)
    print(f"Target: {TARGET['name']} ({TARGET['ticker']})")
    print(f"Target Aug. 31, 2026 close: ${TARGET['price']:,.2f}")
    print(f"Target annual reported GAAP diluted EPS: ${target_eps:,.2f}")
    print()

    usable = []
    for peer in PEERS:
        price, eps = peer["price"], peer["diluted_eps"]
        if not valid_positive(price) or not valid_positive(eps):
            print(f"Excluded from calculation: {peer['ticker']} (missing, zero, or negative price/EPS)")
            continue
        multiple = price / eps
        usable.append((peer, multiple))
        print(f"{peer['name']} ({peer['ticker']}): ${price:,.2f} / ${eps:,.2f} = {multiple:.6f}x")

    if not usable:
        print("\nNo usable peers; no implied price is available.")
        return

    multiples = [multiple for _, multiple in usable]
    if len(usable) == 1:
        peer, multiple = usable[0]
        implied = multiple * target_eps
        print("\nOne valid peer: reference estimate, not a peer range.")
        print(f"Reference peer: {peer['ticker']} at {multiple:.6f}x")
        print(f"Costco implied price: ${implied:,.2f}")
        print("\nPeer-removal sensitivity")
        print(f"Remove {peer['ticker']}: no estimate (no usable peers remain)")
        return

    print("\nPeer P/E range")
    for label, multiple in (("Low", min(multiples)), ("Median", median(multiples)), ("High", max(multiples))):
        print(f"{label}: {multiple:.6f}x; Costco implied price: ${multiple * target_eps:,.2f}")

    print("\nPeer-removal sensitivity")
    full_estimate = median(multiples) * target_eps
    for removed_peer, _ in usable:
        remaining = [multiple for peer, multiple in usable if peer is not removed_peer]
        if not remaining:
            print(f"Remove {removed_peer['ticker']}: no estimate (no usable peers remain)")
            continue
        remaining_estimate = median(remaining) * target_eps
        print(
            f"Remove {removed_peer['ticker']}: ${remaining_estimate:,.2f} "
            f"(${remaining_estimate - full_estimate:+,.2f} vs. full-peer estimate)"
        )


if __name__ == "__main__":
    main()
