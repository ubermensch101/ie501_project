# Portfolio Backtesting Script

This script is designed to backtest a portfolio's performance over a given time period using historical price and shares data. It computes portfolio statistics such as total returns, individual asset performance, and standard deviation, while generating a detailed report in a `stats.txt` file.

---

## Features

1. **Portfolio Statistics**:
   - Total portfolio return (compounded monthly).
   - Portfolio standard deviation of monthly returns.
   - Final portfolio value.
   - Initial and final portfolio capital.

2. **Individual Asset Statistics**:
   - Start and end prices during the backtesting period.
   - Number of shares held.
   - Capital allocated to each asset.
   - Percentage return for each asset.

3. **Clean and Structured Reporting**:
   - Portfolio statistics are placed at the top of the `stats.txt` file.
   - Individual asset statistics are listed in detail.

---

## Input Files

1. **`asset_prices.csv`**:
   Contains historical price data for assets in the portfolio. Each row includes:
   - `Year`, `Month`: Period for the data.
   - Asset names as columns (e.g., `BAJFINANCE.NS`, `HDFCBANK.NS`).
   - Asset-specific monthly returns as columns with suffix `_Return` (e.g., `TCS.NS_Return`).

   **Example**:
   ```
   Year,Month,BAJFINANCE.NS,HDFCBANK.NS,TCS.NS,BAJFINANCE.NS_Return,HDFCBANK.NS_Return,TCS.NS_Return
   2015,January,393.13,498.30,1025.31,,,,
   2015,February,398.62,487.50,1099.80,-0.0652,-0.0217,0.0726
   ```

2. **`shares_allocation.csv`**:
   Specifies the number of shares held for each asset.

   **Example**:
   ```
   Asset,Shares
   BAJFINANCE.NS,5000
   HDFCBANK.NS,3000
   TCS.NS,2000
   ```

---

## Output File

1. **`stats.txt`**:
   - Contains detailed portfolio and asset-level statistics.
   - Starts with overall portfolio performance summary.
   - Includes individual asset statistics such as start price, end price, shares held, capital allocated, and percentage return.

---

## How to Run

1. **Ensure Prerequisites**:
   - Python installed.
   - Required libraries: `pandas`.

2. **Prepare Input Files**:
   - Place `asset_prices.csv` and `shares_allocation.csv` in the script's directory.

3. **Run the Script**:
   ```bash
   python backtest_portfolio.py
   ```

4. **View Results**:
   - Open `stats.txt` to review the backtest report.

---

## Example `stats.txt` Output

```
===== Portfolio Statistics =====
Total Portfolio Capital: 10,000,000.00
Total Portfolio Monthly Return (Compounded): 54.30%
Portfolio Standard Deviation: 3.45
Final Portfolio Value: 15,430,000.00

Asset: BAJFINANCE.NS
  Start Price: 393.13
  End Price: 1099.80
  Shares Held: 5000
  Capital Allocated: 3,533,350.00
  Percentage Return: 179.79%

Asset: HDFCBANK.NS
  Start Price: 498.30
  End Price: 487.50
  Shares Held: 3000
  Capital Allocated: -32,400.00
  Percentage Return: -2.17%

...
```

---

## Notes

- The script assumes that the `shares_allocation.csv` file accurately reflects the number of shares held throughout the backtesting period.
- Ensure that the `asset_prices.csv` data covers the desired backtesting time frame.

---

## Future Improvements

- Allow dynamic time periods for backtesting.
- Add visualization of portfolio growth and individual asset performance.
- Support for dividends or other adjustments.

---
