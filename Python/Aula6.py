import pandas as pd
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
#lê a página e cria a lista em dfs
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))
#dfs é do tipo lista e tem apenas de comprimento
#cria a variável que contem o DataFrame do síte

df_bancos = dfs[0]

print(df_bancos.shape)
#mostra a quantidade de línhas e colunas
print(df_bancos.dtypes)
#agora temos os indices

print(df_bancos.head())
