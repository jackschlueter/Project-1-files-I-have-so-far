"""P/E comparable-company valuation exercise.

Edit TARGET and PEERS below.  All inputs are intentionally local; this script
does not fetch market data and does not use cash or debt in a P/E valuation.
"""

from __future__ import annotations

from statistics import median
from typing import Any


# ------------------------------ EDIT INPUTS ------------------------------
TARGET = {
    "ticker": "ABG",
    "name": "Asbury Automotive Group",
    "price": 243.03,
    "diluted_eps": 21.50,
}

PEERS = [
    {
        "ticker": "AN",
        "name": "AutoNation",
        "price": 169.84,
        "diluted_eps": 16.92,
    },
    {
        "ticker": "GPI",
        "name": "Group 1 Automotive",
        "price": 421.48,
        "diluted_eps": 36.81,
    },
]
# -------------------------------------------------------------------------


def text(value: Any) -> str:
    """Return a safe display string for an editable input."""
    return "missing" if value is None else str(value)


def positive_number(record: dict[str, Any], field: str) -> float | None:
    """Return a positive numeric input, otherwise None."""
    value = record.get(field)
    if isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if number > 0 else None


def identifier(record: dict[str, Any]) -> str:
    """Use ticker as the peer identity; fall back to a name if needed."""
    value = record.get("ticker") or record.get("name")
    return str(value).strip().upper()


def display_name(record: dict[str, Any]) -> str:
    return f"{record.get('name', 'Unnamed peer')} ({record.get('ticker', 'no ticker')})"


def implied_price(multiple: float, target_eps: float | None) -> float | None:
    return None if target_eps is None else multiple * target_eps


def price_display(value: float | None) -> str:
    return "not meaningful" if value is None else f"${value:,.2f}"


def main() -> None:
    target_id = identifier(TARGET)
    target_eps = positive_number(TARGET, "diluted_eps")
    target_price = positive_number(TARGET, "price")

    print("P/E Comparable-Company Valuation")
    print("=" * 34)
    print(f"Target: {display_name(TARGET)}")
    print(f"Target closing price: {price_display(target_price)}")
    if target_eps is None:
        print("Target diluted EPS: not meaningful (missing or nonpositive)")
    else:
        print(f"Target diluted EPS: ${target_eps:,.6f}")
    print()

    unique_peers: list[dict[str, Any]] = []
    seen: set[str] = set()
    for peer in PEERS:
        peer_id = identifier(peer)
        if not peer_id:
            print(f"Excluded peer with no ticker or name: {peer}")
        elif peer_id == target_id:
            print(f"Excluded target from peer set: {display_name(peer)}")
        elif peer_id in seen:
            print(f"Excluded duplicate peer: {display_name(peer)}")
        else:
            seen.add(peer_id)
            unique_peers.append(peer)

    peer_multiples: list[tuple[dict[str, Any], float | None]] = []
    print("Peer P/E calculations")
    for peer in unique_peers:
        price = positive_number(peer, "price")
        eps = positive_number(peer, "diluted_eps")
        pe = None if price is None or eps is None else price / eps
        peer_multiples.append((peer, pe))
        if pe is None:
            print(
                f"- {display_name(peer)}: not meaningful "
                f"(price={text(peer.get('price'))}, diluted EPS={text(peer.get('diluted_eps'))})"
            )
        else:
            print(f"- {display_name(peer)}: {pe:.6f}x")
    print()

    usable = [(peer, pe) for peer, pe in peer_multiples if pe is not None]
    if not usable:
        print("No usable peers; no implied-price estimate is available.")
        return

    multiples = [pe for _, pe in usable]
    low_multiple = min(multiples)
    median_multiple = median(multiples)
    high_multiple = max(multiples)
    full_estimate = implied_price(median_multiple, target_eps)

    if len(usable) == 1:
        peer, multiple = usable[0]
        print(f"One valid peer: {display_name(peer)} is a reference estimate, not a range.")
        print(f"Reference P/E: {multiple:.6f}x")
        print(f"Median-implied target price: {price_display(full_estimate)}")
    else:
        print(f"Usable peers: {len(usable)}")
        print(f"Minimum peer P/E: {low_multiple:.6f}x")
        print(f"Median peer P/E:  {median_multiple:.6f}x")
        print(f"Maximum peer P/E: {high_multiple:.6f}x")
        print(f"Implied price at minimum P/E: {price_display(implied_price(low_multiple, target_eps))}")
        print(f"Implied price at median P/E:  {price_display(full_estimate)}")
        print(f"Implied price at maximum P/E: {price_display(implied_price(high_multiple, target_eps))}")

    print()
    print("Peer-removal sensitivity")
    for removed_peer, _ in peer_multiples:
        remaining = [
            pe for peer, pe in peer_multiples if peer is not removed_peer and pe is not None
        ]
        if not remaining:
            print(f"- Remove {display_name(removed_peer)}: no estimate (no usable peers remain)")
            continue
        remaining_estimate = implied_price(median(remaining), target_eps)
        change = None
        if full_estimate is not None and remaining_estimate is not None:
            change = remaining_estimate - full_estimate
        change_display = "not meaningful" if change is None else f"${change:+,.2f}"
        print(
            f"- Remove {display_name(removed_peer)}: "
            f"{price_display(remaining_estimate)} ({change_display} vs. full-peer estimate)"
        )


if __name__ == "__main__":
    main()
