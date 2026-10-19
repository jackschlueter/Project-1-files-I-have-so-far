"""Calculate Costco's beta relative to the S&P 500 using weekly returns.

Run:
    python3 costco_beta.py

Install the one data dependency if needed:
    python3 -m pip install yfinance

Beta = covariance(COST returns, S&P 500 returns) / variance(S&P 500 returns)
"""

STOCK_TICKER = "COST"
MARKET_TICKER = "^GSPC"  # S&P 500 index
PERIOD = "5y"
INTERVAL = "1wk"


def get_closes(ticker):
    """Download adjusted closing prices and return a date-to-price dictionary."""
    import yfinance as yf

    prices = yf.download(
        ticker,
        period=PERIOD,
        interval=INTERVAL,
        auto_adjust=True,
        progress=False,
    )["Close"]

    # yfinance may return a one-column DataFrame instead of a Series.
    if hasattr(prices, "columns"):
        prices = prices.iloc[:, 0]

    return {date: float(price) for date, price in prices.items()}


def returns_from_prices(prices):
    """Turn ordered prices into simple percentage returns by date."""
    dates = sorted(prices)
    return {
        dates[index]: prices[dates[index]] / prices[dates[index - 1]] - 1.0
        for index in range(1, len(dates))
    }


def calculate_beta(stock_returns, market_returns):
    """Calculate sample beta from aligned return observations."""
    common_dates = sorted(set(stock_returns) & set(market_returns))
    if len(common_dates) < 2:
        raise ValueError("Need at least two matching return observations.")

    stock = [stock_returns[date] for date in common_dates]
    market = [market_returns[date] for date in common_dates]
    stock_mean = sum(stock) / len(stock)
    market_mean = sum(market) / len(market)

    covariance = sum(
        (stock_return - stock_mean) * (market_return - market_mean)
        for stock_return, market_return in zip(stock, market)
    ) / (len(common_dates) - 1)
    market_variance = sum(
        (market_return - market_mean) ** 2 for market_return in market
    ) / (len(common_dates) - 1)

    if market_variance == 0:
        raise ValueError("Market-return variance is zero; beta is undefined.")
    return covariance / market_variance, len(common_dates)


def main():
    try:
        costco_returns = returns_from_prices(get_closes(STOCK_TICKER))
        market_returns = returns_from_prices(get_closes(MARKET_TICKER))
        beta, observations = calculate_beta(costco_returns, market_returns)
    except ImportError:
        print("Missing package: run python3 -m pip install yfinance, then try again.")
        return
    except Exception as error:
        print(f"Could not calculate beta: {error}")
        return

    print(f"Costco beta vs. S&P 500: {beta:.3f}")
    print(f"Period: {PERIOD}; interval: {INTERVAL}; matched returns: {observations}")
    print("This is historical beta, not a guarantee of future risk or return.")


if __name__ == "__main__":
    main()
