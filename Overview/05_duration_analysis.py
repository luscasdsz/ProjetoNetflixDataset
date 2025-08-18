#imports necesssarios

import pandas as pd
import matplotlib.pyplot as plt

#chamando o dataset original do github
csv_url = "https://raw.githubusercontent.com/luscasdsz/ProjetoNetflixDataset/main/data/Netflix%20Dataset.csv"
csv = pd.read_csv(csv_url, sep=',',encoding='utf-8')

#processamento de dados
#tratamento de nulos
csv['Country'] = csv['Country'].fillna('unknown')
csv['Rating'] = csv['Rating'].fillna('unrated')

#criação do objeto final
netflix = csv[['Category','Title','Country','Release_Date','Rating','Duration','Type']]
#copia dos valores que são filmes dentro da coluna de categorias (que define se é filme ou tv show
filmes = netflix[netflix['Category'] == "Movie"].copy()
#os valores da coluna de duração estavam como strings e causando erros, aqui eu transformo eles em float e retiro o 'min'
filmes['Duration_min'] = filmes['Duration'].str.replace(' min','').astype(float)
#bins aqui funcionam como caixinhas de duração para filtrar as durações de filmes
bins = [0,60,90,120,180, filmes['Duration_min'].max()]
#aqui eu decido como as bins vão aparecer no grafico, pois no meu dataframe eu chamei elas pelas durações
labels = ['<=60 min', '61-90 min', '91-120 min', '121-180 min', '>180 min']
#aqui eu dou a cada duração sua bin adequada
filmes['Duration_bin'] = pd.cut(filmes['Duration_min'], bins=bins, labels=labels, include_lowest=True)
#este vai ser o objeto para a produção do grafico
duration_counts = filmes['Duration_bin'].value_counts().sort_index()

#figura do grafico e detalhes do grafico
plt.figure(figsize = (15,10))
duration_counts.plot(kind='bar', color=['blue', 'green', 'red'], title='Distribuição da duração dos filmes na Netflix')
plt.ylabel('Quantidade de filmes')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

#criação de contagem ao lado das barras
for i, v in enumerate(duration_counts):
    plt.text(i, v+20, str(v), ha='center', fontweight='bold')

#salvar para portfolio
plt.savefig('outputs/figures/Distribuição de durações de filmes da netflix.png', dpi=300, bbox_inches='tight')
plt.show()