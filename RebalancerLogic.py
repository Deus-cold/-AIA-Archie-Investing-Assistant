def recommend_rebalancing(portfolio, targets):
    recommendations = {}
    total_value = sum(asset['value'] for asset in portfolio)

    for asset in portfolio:
        ticker = asset['ticker']
        current_pct = asset['value']/  total_value
        target_pct = targets.get(ticker, current_pct) # default to current if missing 
        diff = target_pct - current_pct
        recommendations[ticker] = round(diff * total_value, 2) # how much to buy/sell

    return recommendations

