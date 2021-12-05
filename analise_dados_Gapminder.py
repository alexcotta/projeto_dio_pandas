import pandas as pd
import matplotlib.pyplot as plt 


def exibe(descricao, resultado_comando):
    print(descricao +'\n', resultado_comando)


def visualizacao(valor, titulo, xlabel, ylabel):
    plt.plot(valor)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
# Carregamento do arquivo para analise exploratória
df = pd.read_csv('datasets/Gapminder.csv', sep=";")

# Qunatidade linhas e colunas na tabela
exibe(">> Quantidade de linhas e colunas da tabela: ", df.shape)

# Nome das colunas
exibe(">> Nome das colunas da tabela: ", df.columns)

# informa estatisticas da tabela
exibe(">> Estatisticas da tabela: ",df.describe())

# verifica se tem valores nulos na tabela
exibe(">> Quantidade de valores nulos encontrados em cada campo da tabela: ",
      df.isnull().sum())

# modificando os nomes das colunas
df = df.rename(columns={'country':'pais', 'continent':'continente', 'year':'ano',
                        'lifeExp':'expectativa de vida','pop':'população',
                        'gdpPercap':'renda per capita'})
exibe(">> ", df.columns)

# agrupamento de resultados
exibe(">> ",df.groupby('continente')['pais'].unique())

# agrupamento com contagem de cada grupo
exibe(">> ", df.groupby('continente')['pais'].nunique())

# renda per capita média por continente
df.groupby('continente')['renda per capita'].mean()
continentes = df['continente']

# Renda per capita ao longo dos anos
expectativa = df.groupby('ano')['renda per capita'].mean()
visualizacao(expectativa, 'Renda per capita ao longo dos anos.',
             'Ano', 'Média renda per capita')

# Expectativa de vida média ao longo dos anos
expectativa = df.groupby('ano')['expectativa de vida'].mean()
visualizacao(expectativa, 'Expectativa de vida ao longo dos anos.', 'Ano',
             'Média expectativa de vida.')


