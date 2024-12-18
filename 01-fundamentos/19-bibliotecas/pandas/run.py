import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("./ABEV3_OHLC.csv", sep=";")

print("cabecalho com cinco linhas",dados.head())
print("total de linhas e colunas",dados.shape)
print("tipos de dados",dados.dtypes)
print("últimas linhas",dados.tail())

#=======================================================

cols_numericas = ["Open", "High", "Low", "Close"]
for col in cols_numericas:
    dados[col] = pd.to_numeric(dados[col].str.replace(",", "").str.strip(), errors="coerce")

# Gera o gráfico
dados["Close"].plot(title="Gráfico de Fechamento")
plt.show()  # Necessário para exibir o gráfico

