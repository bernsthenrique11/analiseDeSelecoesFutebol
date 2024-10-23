import kaggle
import pandas as pd
import kagglehub # PARA IMPORTAR O DATABASE
import os
import matplotlib.pyplot as plt


# DEFININDO O CAMINHO ONDE OS ARQUIVOS DEVERÃO SER BAIXADOS
caminho_download = "C:/Users/henrique.bernst_priv/PycharmProjects/futebolProject"
arquivos = os.listdir(caminho_download)
print("Arquivos dentro da pasta", arquivos)

if not os.path.exists(caminho_download):
    os.makedirs(caminho_download)

# REALIZANDO O DOWNLOAD DA ÚLTIMA VERSÃO
kaggle.api.dataset_download_files('martj42/international-football-results-from-1872-to-2017', path=caminho_download, unzip=True)

print(f"Caminho para os arquivos do dataset: {caminho_download}")

# CARREGANDO O DATASET
df_resultados = pd.read_csv("C:/Users/henrique.bernst_priv/PycharmProjects/futebolProject/results.csv") # RESULTADOS
df_marcadores_gol = pd.read_csv("C:/Users/henrique.bernst_priv/PycharmProjects/futebolProject/goalscorers.csv") # JOGADORES QUE MARCARAM GOLS NO JOGO
df_penaltis = pd.read_csv("C:/Users/henrique.bernst_priv/PycharmProjects/futebolProject/shootouts.csv") # DISPUTA POR PENALTIS

# VERIFICANDO VALORES FALTANTES

df_resultados = df_resultados.drop_duplicates()
df_marcadores_gol = df_marcadores_gol.drop_duplicates()
df_penaltis = df_penaltis.drop_duplicates()

# CÁLCULO DE DESEMPENHO

# JOGOS EM QUE O TIME DA CASA VENCEU
casa_venceu = df_resultados[df_resultados['home_score'] > df_resultados['away_score']].groupby('home_team').size()

# JOGOS EM QUE O TIME VISITANTE VENCEU
visitante_venceu = df_resultados[df_resultados['away_score'] > df_resultados['home_score']].groupby('away_team').size()

# JUNTANDO OS RESULTADOS
total_de_vitorias = casa_venceu.add(visitante_venceu, fill_value=0)

# FILTRO DE VITÓRIAS POR SELEÇÃO
selecoes_mais_de_x_vitorias = total_de_vitorias[total_de_vitorias > x] # SUBSTITUA X PELO VALOR DE VITÓRIAS DESEJADO

# REALIZANDO A CONTAGEM DE EMPATES
empates = df_resultados[df_resultados['home_score'] == df_resultados['away_score']].groupby(['home_team']).size()


# GOLS MARCADOS EM CASA E FORA
gols_casa = df_resultados.groupby('home_team')['home_score'].sum()
gols_visitante = df_resultados.groupby('away_team')['away_score'].sum()

# GOLS SOFRIDOS EM CASA E FORA
gols_concedidos_casa = df_resultados.groupby('home_team')['away_score'].sum()
gols_concedidos_visitante = df_resultados.groupby('away_team')['home_score'].sum()

# SOMA TOTAL DE GOLS MARCADOS
gols_total = gols_casa.add(gols_visitante, fill_value=0)
gols_total_concedidos = gols_concedidos_casa.add(gols_concedidos_visitante, fill_value=0)


# --- #

# CRIANDO O GRÁFICO DE VITÓRIAS (GRÁFICO DE BARRAS)

total_de_vitorias.sort_values(ascending=False).plot(kind='bar', figsize=(10,6), title='Número de vitórias por Seleção')
plt.xlabel('Seleção')
plt.ylabel('Vitórias')
plt.show()

# GRÁFICO DE GOLS MARCADOS

gols_total.sort_values(ascending=False).plot(kind='bar', figsize=(10,6), title='Gols Marcados Por Seleção')
plt.xlabel('Seleção')
plt.ylabel('Gols Marcados')
plt.show()

# CRIANDO O GRÁFICO DE VITÓRIAS FILTRADAS POR SELEÇÃO
selecoes_mais_de_x_vitorias.sort_values(ascending=False).plot(kind='bar', figsize=(10,6), title='Número de vitórias por Seleção')
plt.xlabel('Seleção')
plt.ylabel('Vitórias')
plt.show()

