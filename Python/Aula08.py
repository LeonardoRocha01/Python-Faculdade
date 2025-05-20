import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Defini os intervalos de tempo
data_fim = datetime.today()
data_inicio = data_fim - timedelta(days=365 * 10)
data_inicio_str = data_inicio.strftime('%d/%m/%Y')
data_fim_str = data_fim.strftime('%d/%m/%Y')

#URL da API com o intervalo de datas definido
url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial={data_inicio_str}&dataFinal={data_fim_str}"

#Carregar dados JSON com pandas
df = pd.read_json(url)

#Converte as colunas para os tipos corretos
df['data'] = pd.to_datetime(df['data'], dayfirst=True)
df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

#Adicionar coluna de ano
df['ano'] = df['data'].dt.year

#Calcular média anul da Selic
media_anual = df.groupby('ano')['valor'].mean()

#Plotar gráfico de barras
plt.figure(figsize=(12,6))
media_anual.plot(kind='bar',color='royalblue', edgecolor='black')

#Personalizações do gráfico 
plt.title('Média Anul da Taxa Selic - Último 10 anos', fontsize=16, fontweight='bold')
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Taxa selic Média (%}', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

#Mostra o gráfico
plt.show()
