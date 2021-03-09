import robin_stocks.robinhood as rh
import math

def get_stocks_as_percent(holdings):
    holdings_pct = []
    total_value = 0.0
    for k, value in holdings.items():
        total_value += float(value['equity'])
    for k, value in holdings.items():
        holdings_pct.append({
            "name": k,
            "equity": math.floor(100 * (float(value['equity']) / total_value) )
        })
    holdings_pct.sort(key=lambda x: x['equity'])
    # other_item = {"name":"Other", "equity":0.0}
    # while len(holdings_pct) > max_results:
    #     other_item["equity"] += holdings_pct[-1]['equity']
    #     del holdings_pct[-1]
    # holdings_pct.append(other_item)
    # # assert len(holdings_pct) <= max_results
    return holdings_pct

def get_profile_data(username):
    holdings = rh.build_holdings()
    return get_stocks_as_percent(holdings)


details = rh.login("EMAIL HERE", "PASSWORD HERE")