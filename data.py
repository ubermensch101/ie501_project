# Define assets and sectors
assets_sectors = {
    'RELIANCE.NS': 'Energy',
    'TCS.NS': 'IT',
    'HDFCBANK.NS': 'Financials',
    'INFY.NS': 'IT',
    'ICICIBANK.NS': 'Financials',
    'BAJFINANCE.NS': 'Financials',
    'HINDUNILVR.NS': 'Consumer Goods',
    'ITC.NS': 'Consumer Goods',
    'TATAMOTORS.NS': 'Automobile',
    'SBIN.NS': 'Financials'
}

assets = list(assets_sectors.keys())
sectors = list(assets_sectors.values())

# Constraints
max_risk = 0.10  # Max portfolio risk (standard deviation)
max_weight = 0.25  # Max weight for any single asset

total_capital = 10000000  # 10,000,000 INR

