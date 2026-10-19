"""Check the Meridian Foundation Reserve candidates against measurable rules."""

from math import isclose


# Editable case inputs. All candidate weights are percentages of the portfolio.
HOLDINGS = {
    "Cash": {"issuer": "none", "redeem_days": 0, "reserve_eligible": True},
    "Treasury bills": {
        "issuer": "U.S. Treasury",
        "redeem_days": 1,
        "reserve_eligible": True,
    },
    "Treasury 10-year note": {
        "issuer": "U.S. Treasury",
        "redeem_days": 1,
        "reserve_eligible": True,
    },
    "Global equity index fund": {
        "issuer": "diversified fund",
        "redeem_days": 2,
        "reserve_eligible": False,
    },
    "Investment-grade bond fund": {
        "issuer": "diversified fund",
        "redeem_days": 3,
        "reserve_eligible": False,
    },
    "Private real estate fund": {
        "issuer": "diversified fund",
        "redeem_days": 90,
        "reserve_eligible": False,
    },
    "Acme Corp bonds": {
        "issuer": "Acme Corp",
        "redeem_days": 4,
        "reserve_eligible": False,
    },
    "Acme Corp stock": {
        "issuer": "Acme Corp",
        "redeem_days": 1,
        "reserve_eligible": False,
    },
}

CANDIDATES = {
    "A": {
        "Cash": 2,
        "Treasury bills": 2,
        "Treasury 10-year note": 10,
        "Global equity index fund": 60,
        "Investment-grade bond fund": 26,
        "Private real estate fund": 0,
        "Acme Corp bonds": 0,
        "Acme Corp stock": 0,
    },
    "B": {
        "Cash": 1,
        "Treasury bills": 0,
        "Treasury 10-year note": 0,
        "Global equity index fund": 55,
        "Investment-grade bond fund": 20,
        "Private real estate fund": 15,
        "Acme Corp bonds": 5,
        "Acme Corp stock": 4,
    },
    "C": {
        "Cash": 1,
        "Treasury bills": 1,
        "Treasury 10-year note": 0,
        "Global equity index fund": 70,
        "Investment-grade bond fund": 20,
        "Private real estate fund": 0,
        "Acme Corp bonds": 0,
        "Acme Corp stock": 8,
    },
    "D": {
        "Cash": 100,
        "Treasury bills": 0,
        "Treasury 10-year note": 0,
        "Global equity index fund": 0,
        "Investment-grade bond fund": 0,
        "Private real estate fund": 0,
        "Acme Corp bonds": 0,
        "Acme Corp stock": 0,
    },
}

RESERVE_SIZE_MILLIONS = 100
QUARTERLY_DISTRIBUTION_MILLIONS = 0.75
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW_DAYS = 5
MIN_LIQUID_SHARE_PERCENT = 90
ISSUER_LIMIT_PERCENT = 8
EXEMPT_ISSUERS = {"none", "U.S. Treasury", "diversified fund"}


def print_check(label, measured, passed):
    print(f"  {label}: {measured:.1f}% — {'pass' if passed else 'FAIL'}")
    return not passed


def main():
    reserve_minimum = (
        QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION_MILLIONS
        / RESERVE_SIZE_MILLIONS * 100
    )
    print(f"Reserve minimum: {reserve_minimum:.1f}%")

    for name, weights in CANDIDATES.items():
        unknown = set(weights) - set(HOLDINGS)
        if unknown:
            raise ValueError(f"Candidate {name} has unknown holdings: {sorted(unknown)}")

        total = sum(weights.values())
        lowest = min(weights.values())
        reserve = sum(
            weight for holding, weight in weights.items()
            if HOLDINGS[holding]["reserve_eligible"]
        )
        liquid = sum(
            weight for holding, weight in weights.items()
            if HOLDINGS[holding]["redeem_days"] <= LIQUIDITY_WINDOW_DAYS
        )

        company_totals = {}
        for holding, weight in weights.items():
            issuer = HOLDINGS[holding]["issuer"]
            if issuer not in EXEMPT_ISSUERS:
                company_totals[issuer] = company_totals.get(issuer, 0) + weight
        largest_company = max(company_totals.values(), default=0)

        print(f"\nCandidate {name}")
        failures = 0
        failures += print_check("Weights sum to 100", total,
                                isclose(total, 100, rel_tol=0, abs_tol=1e-9))
        failures += print_check("Lowest weight (long-only)", lowest, lowest >= 0)
        failures += print_check("Reserve-eligible weight", reserve,
                                reserve >= reserve_minimum)
        failures += print_check("Redeemable within window", liquid,
                                liquid >= MIN_LIQUID_SHARE_PERCENT)
        failures += print_check("Largest single company", largest_company,
                                largest_company <= ISSUER_LIMIT_PERCENT)
        print("  Calendar-year loss: requires CIO clarification")
        if failures == 0:
            print("  passes every checkable rule")
        else:
            print(f"  fails {failures} rule(s)")


if __name__ == "__main__":
    main()
