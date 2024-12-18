import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Baixar dados históricos da ação
ticker = "PETR4.SA"  # Ticker da ação - deve ter .SA
#dados = yf.download(ticker, start="2020-01-01", end="2024-01-01")
#dados.to_csv("PETR_OHLC.csv")  # Salvar como CSV

petr = pd.read_csv("PETR_OHLC.csv",sep=',')

# cols_numericas = ['Price', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
# for col in cols_numericas:
#     petr[col] = pd.to_numeric(petr[col].str.replace(",", "").str.strip(), errors="coerce")

# petr.plot()
# plt.show()

print(petr)
