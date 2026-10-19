# Inputs (USD millions, except percentages and per-share values).
STARTING_FCFF = 7952.3
# FY2023-FY2025 net-sales CAGR from Costco's FY2025 Form 10-K.
GROWTH_RATES = (0.065583, 0.065583, 0.065583, 0.065583, 0.065583)
# Placeholder: unresolved because Costco's 10-K does not provide a cost of equity.
WACC = 0.10
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 14161.0
DEBT = 5805.0
DILUTED_SHARES = 444.803

# Editable sensitivity and reverse-DCF settings.
SENSITIVITY_WACCS = (0.09, 0.10, 0.11)
SENSITIVITY_TERMINAL_GROWTHS = (0.02, 0.03, 0.04)
TARGET_SHARE_PRICE = 902.75
REVERSE_SHIFT_LOWER_BOUND = -0.05
REVERSE_SHIFT_UPPER_BOUND = 0.10


def value_per_share(wacc, terminal_growth, growth_rates=GROWTH_RATES):
	if terminal_growth >= wacc:
		return None

	fcff = []
	value = STARTING_FCFF
	for growth in growth_rates:
		value *= 1.0 + growth
		fcff.append(value)

	present_value_explicit = sum(
		cash_flow / (1.0 + wacc) ** year
		for year, cash_flow in enumerate(fcff, start=1)
	)
	terminal_value = fcff[-1] * (1.0 + terminal_growth) / (wacc - terminal_growth)
	present_value_terminal = terminal_value / (1.0 + wacc) ** len(fcff)
	enterprise_value = present_value_explicit + present_value_terminal
	equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
	return equity_value / DILUTED_SHARES


def print_sensitivity_grid():
	print("\nSensitivity grid: value per diluted share")
	header = "WACC \\ terminal growth".ljust(24)
	header += "".join(f"{growth:.0%}".rjust(12) for growth in SENSITIVITY_TERMINAL_GROWTHS)
	print(header)
	for wacc in SENSITIVITY_WACCS:
		row = f"{wacc:.0%}".ljust(24)
		for terminal_growth in SENSITIVITY_TERMINAL_GROWTHS:
			value = value_per_share(wacc, terminal_growth)
			cell = "invalid" if value is None else f"{value:.2f}"
			row += cell.rjust(12)
		print(row)


def print_reverse_dcf():
	lower = REVERSE_SHIFT_LOWER_BOUND
	upper = REVERSE_SHIFT_UPPER_BOUND
	if any(growth + lower <= -1.0 or growth + upper <= -1.0 for growth in GROWTH_RATES):
		print("\nReverse DCF: invalid bracket; a growth rate reaches -100% or below.")
		return

	def price_for_shift(shift):
		shifted_growth_rates = tuple(growth + shift for growth in GROWTH_RATES)
		return value_per_share(WACC, TERMINAL_GROWTH, shifted_growth_rates)

	lower_price = price_for_shift(lower)
	upper_price = price_for_shift(upper)
	print("\nReverse DCF: uniform shift to all five explicit growth rates")
	print(f"Target share price: {TARGET_SHARE_PRICE:.2f}")
	print(
		"Held fixed: "
		f"starting FCFF={STARTING_FCFF:.1f}, WACC={WACC:.2%}, "
		f"terminal growth={TERMINAL_GROWTH:.2%}, cash={NON_OPERATING_CASH:.1f}, "
		f"debt={DEBT:.1f}, diluted shares={DILUTED_SHARES:.3f}"
	)
	print(f"Search bracket: {lower:+.2%} to {upper:+.2%}")

	if not min(lower_price, upper_price) <= TARGET_SHARE_PRICE <= max(lower_price, upper_price):
		print("No solution in this bracket.")
		return

	for _ in range(100):
		midpoint = (lower + upper) / 2.0
		midpoint_price = price_for_shift(midpoint)
		if abs(midpoint_price - TARGET_SHARE_PRICE) < 0.000001:
			break
		if midpoint_price < TARGET_SHARE_PRICE:
			lower = midpoint
		else:
			upper = midpoint

	print(f"Solved uniform growth-rate shift: {midpoint:+.4%}")
	print(f"Value per diluted share at solved shift: {midpoint_price:.2f}")


def main():
	if TERMINAL_GROWTH >= WACC:
		print("Error: terminal growth must be less than WACC.")
		return

	fcff = []
	value = STARTING_FCFF
	for growth in GROWTH_RATES:
		value *= 1.0 + growth
		fcff.append(value)

	present_value_explicit = sum(
		cash_flow / (1.0 + WACC) ** year
		for year, cash_flow in enumerate(fcff, start=1)
	)
	terminal_value = fcff[-1] * (1.0 + TERMINAL_GROWTH) / (WACC - TERMINAL_GROWTH)
	present_value_terminal = terminal_value / (1.0 + WACC) ** len(fcff)
	enterprise_value = present_value_explicit + present_value_terminal
	equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
	value_per_share = equity_value / DILUTED_SHARES
	terminal_share = present_value_terminal / enterprise_value

	for year, cash_flow in enumerate(fcff, start=1):
		print(f"FCFF year {year}: {cash_flow:.4f}")
	print(f"Present value of 5 explicit FCFF: {present_value_explicit:.4f}")
	print(f"Terminal value at year 5: {terminal_value:.4f}")
	print(f"Present value of terminal value: {present_value_terminal:.4f}")
	print(f"Enterprise value: {enterprise_value:.4f}")
	print(f"Equity value: {equity_value:.4f}")
	print(f"Value per diluted share: {value_per_share:.4f}")
	print(f"PV of terminal value as share of enterprise value: {terminal_share:.4f}")
	print_sensitivity_grid()
	print_reverse_dcf()


if __name__ == "__main__":
	main()
