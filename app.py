import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="NSE-BSE Arbitrage", layout="wide")
st.title("📈 NSE vs BSE Arbitrage Opportunities")

# -- Configuration --
STOCK_LIST = [getAllStockSymbols(): Promise<string[]>]
THRESHOLD = 0.5  # Minimum price difference in ₹ to consider arbitrage

# -- Dummy function to simulate API call --
def fetch_price(exchange, symbol):
    # Replace this with a real API call
    dummy_data = {
        "RELIANCE": {"NSE": 2800.50, "BSE": 2802.20},
        "INFY": {"NSE": 1488.75, "BSE": 1489.90},
        "TCS": {"NSE": 3700.25, "BSE": 3699.20},
        "HDFCBANK": {"NSE": 1675.80, "BSE": 1676.10},
        "SBIN": {"NSE": 590.25, "BSE": 591.40},
        "ITC": {"NSE": 445.10, "BSE": 444.00}
    }
    return dummy_data[symbol][exchange]

# -- Analysis --
arbitrage_data = []
for stock in STOCK_LIST:
    nse_price = fetch_price("NSE", stock)
    bse_price = fetch_price("BSE", stock)
    diff = round(abs(nse_price - bse_price), 2)
    if diff >= THRESHOLD:
        direction = "Buy NSE, Sell BSE" if nse_price < bse_price else "Buy BSE, Sell NSE"
        arbitrage_data.append({
            "Stock": stock,
            "NSE Price": nse_price,
            "BSE Price": bse_price,
            "Difference": diff,
            "Action": direction
        })

df = pd.DataFrame(arbitrage_data)

# -- Display --
if not df.empty:
    st.success(f"{len(df)} Arbitrage Opportunities Found:")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No arbitrage opportunities above ₹{:.2f}".format(THRESHOLD))

st.caption("Last updated: {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
