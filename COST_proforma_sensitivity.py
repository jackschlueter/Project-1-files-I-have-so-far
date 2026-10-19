"""Run isolated one-input COST sensitivities on the existing linked pro-forma."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "COST_three_statement_2026_2030.py"
BASE_PATH = HERE / "COST_proforma_sensitivity_base_inputs.json"
DETAIL_PATH = HERE / "COST_proforma_sensitivity_details.json"
DRIVERS = (
    ("Paid-member growth", "PAID_MEMBER_GROWTH", "% per year", (0.053, 0.063, 0.073)),
    ("Warehouse footprint", "WAREHOUSE_SQFT_PER_STORE", "sq ft per warehouse", (146_000.0, 147_000.0, 148_000.0)),
)
CHECK_FIELDS = ("balance_gap", "cash_gap", "ppe_gap", "debt_gap", "equity_gap")
LEVELS = ("lower", "base", "higher")


def load_base():
    base = json.loads(BASE_PATH.read_text())
    actual_hash = hashlib.sha256(MODEL_PATH.read_bytes()).hexdigest()
    if actual_hash != base["source_sha256"]:
        raise ValueError("Base input file does not match the saved model source hash")
    return base


def fresh_model(run_id):
    spec = importlib.util.spec_from_file_location(f"cost_proforma_{run_id}", MODEL_PATH)
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    return model


def run_case(base, run_id, driver=None, level=None, value=None):
    # Every call starts from a separate copy of the entire saved base set and
    # a newly loaded model module; no scenario can inherit a previous change.
    inputs = copy.deepcopy(base)
    if driver is not None:
        inputs["base_assumptions"][driver] = value
    model = fresh_model(run_id)
    model.OPENING = copy.deepcopy(inputs["opening"])
    model.DEBT_REPAYMENTS = {int(year): amount for year, amount in inputs["debt_repayments"].items()}
    for name, setting in inputs["base_assumptions"].items():
        setattr(model, name, setting)

    result = {
        "run_id": run_id, "driver": driver, "level": level,
        "changed_value": value, "inputs": inputs,
        "status": "invalid", "valuation_status": "unavailable",
        "error": None, "rows": [], "checks": [],
        "operating_income": None, "fcfe": None, "value_per_share": None,
    }
    try:
        rows = model.forecast()
        result["rows"] = rows
        result["checks"] = [
            {"year": row["year"], **{key: row[key] for key in CHECK_FIELDS},
             "minimum_cash_headroom": row["minimum_cash_headroom"]}
            for row in rows
        ]
        model.check(rows)
        result["status"] = "valid"
        result["operating_income"] = rows[-1]["ebit"]
        result["fcfe"] = rows[-1]["fcfe"]
        if any(row["fcfe"] < 0 for row in rows):
            # The existing valuation clips negative explicit-year FCFE; do not
            # use it for those cases. Keep all signed statement cash flows.
            result["valuation_status"] = "unavailable: negative forecast-year FCFE"
        else:
            try:
                equity_value = model.value_equity(rows)[-1]
                result["value_per_share"] = equity_value / model.SHARES_MILLIONS
                result["valuation_status"] = "valid classroom-model value"
            except (AssertionError, ValueError) as exc:
                result["valuation_status"] = f"unavailable: {exc}"
    except (AssertionError, ValueError, KeyError) as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    return result


def number(value, decimals=1):
    return "unavailable" if value is None else f"{value:,.{decimals}f}"


def change(value, base_value, decimals=1):
    # Recompute from the values displayed in the same table so a listener can
    # reproduce each signed difference without hidden rounding digits.
    return "unavailable" if value is None or base_value is None else f"{round(value, decimals) - round(base_value, decimals):+,.{decimals}f}"


def input_label(driver, value):
    return f"{value * 100:.1f}% per year" if driver == "PAID_MEMBER_GROWTH" else f"{value:,.0f} sq ft/warehouse"


def show_case(result, initial):
    print(
        f"{result['level']:<7} {input_label(result['driver'], result['changed_value']):<25} "
        f"{number(result['operating_income']):>12} {change(result['operating_income'], initial['operating_income']):>12} "
        f"{number(result['fcfe']):>12} {change(result['fcfe'], initial['fcfe']):>12} "
        f"{number(result['value_per_share'], 2):>12} {change(result['value_per_share'], initial['value_per_share'], 2):>12} "
        f"{result['status']}"
    )
    if result["error"] or result["valuation_status"] != "valid classroom-model value":
        print(f"        {result['error'] or result['valuation_status']}")


def show_span(cases):
    spans = []
    for field, decimals in (("operating_income", 1), ("fcfe", 1), ("value_per_share", 2)):
        values = [round(case[field], decimals) for case in cases if case["status"] == "valid" and case[field] is not None]
        spans.append(f"{number(max(values) - min(values), decimals)} ({len(values)}/3 valid)" if values else "unavailable (0/3 valid)")
    print(f"Span, maximum minus minimum: operating income {spans[0]} USD m; FCFE {spans[1]} USD m; value/share {spans[2]} USD")


def show_checks(results):
    print("\nAccounting checks by run and year | gaps and cash headroom in USD millions")
    print(f"{'Run':<25} {'FY':>4} {'BS gap':>12} {'Cash gap':>12} {'PP&E gap':>12} {'Debt gap':>12} {'Equity gap':>12} {'Cash headroom':>15}")
    for result in results:
        if not result["checks"]:
            print(f"{result['run_id']:<25} INVALID: {result['error']}")
            continue
        for row in result["checks"]:
            print(
                f"{result['run_id']:<25} {row['year']:>4} "
                + " ".join(f"{row[key]:>12,.4f}" for key in CHECK_FIELDS)
                + f" {row['minimum_cash_headroom']:>15,.1f}"
            )
        if result["status"] != "valid":
            print(f"{result['run_id']:<25} INVALID: {result['error']}")


def main():
    base = load_base()
    initial = run_case(base, "initial_base")
    if initial["status"] != "valid":
        raise RuntimeError(f"Initial base failed: {initial['error']}")
    results = [initial]
    groups = []
    for title, driver, unit, values in DRIVERS:
        cases = []
        for level, value in zip(LEVELS, values):
            case = run_case(base, f"{driver.lower()}_{level}", driver, level, value)
            cases.append(case)
            results.append(case)
        groups.append((title, driver, unit, cases))
    restored = run_case(base, "restored_base")
    results.append(restored)
    restored_match = (
        restored["status"] == "valid"
        and initial["inputs"] == restored["inputs"]
        and initial["rows"] == restored["rows"]
        and all(initial[key] == restored[key] for key in ("operating_income", "fcfe", "value_per_share"))
    )
    DETAIL_PATH.write_text(json.dumps({
        "model_source_sha256": base["source_sha256"],
        "base_input_file": BASE_PATH.name,
        "units": "USD millions except paid members (millions), footprint (sq ft/warehouse), rates, and USD/share",
        "runs": results, "restored_base_matches_initial": restored_match,
    }, indent=2, allow_nan=False) + "\n")

    print("COST linked pro-forma | one input at a time | FY2026-FY2030")
    print(f"Saved base inputs: {BASE_PATH.name}; full statements and checks: {DETAIL_PATH.name}")
    print("Displayed deltas and spans use displayed rounded outputs (USD m: 0.1; USD/share: 0.01); raw values are saved in the details file")
    print(f"Initial base: FY2030 operating income {number(initial['operating_income'])} USD m; FCFE {number(initial['fcfe'])} USD m; model value/share ${number(initial['value_per_share'], 2)}")
    for title, driver, unit, cases in groups:
        print(f"\n{title} ({driver}; {unit})")
        print("Level   Actual input               Operating m    Delta m       FCFE m    Delta m  Value/share  Delta/share  Checks")
        for case in cases:
            show_case(case, initial)
        show_span(cases)
    print(f"\nRestored base matches initial base: {'PASS' if restored_match else 'FAIL'}")
    print(f"Restored FY2030 operating income {number(restored['operating_income'])} USD m; FCFE {number(restored['fcfe'])} USD m; model value/share ${number(restored['value_per_share'], 2)}")
    show_checks(results)
    if not restored_match:
        raise RuntimeError("Restored base did not match the first run")


if __name__ == "__main__":
    main()
