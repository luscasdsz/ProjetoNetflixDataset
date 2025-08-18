
#imports necessarios
import matplotlib.pyplot as plt
import pandas as pd

#chamando o dataset original do github
csv_url = "https://raw.githubusercontent.com/luscasdsz/ProjetoNetflixDataset/main/data/Netflix%20Dataset.csv"
csv = pd.read_csv(csv_url, sep=',',encoding='utf-8')


#processamento de dados
#tratamento de nulos
csv['Country'] = csv['Country'].fillna('unknown')
csv['Rating'] = csv['Rating'].fillna('unrated')

#criação do objeto final
netflix = csv[['Category','Title','Country','Release_Date','Rating','Duration','Type']]

#criação de tabela cruzada com filmes e series por pais
paises_categoria = netflix.pivot_table(index='Country',
                                       columns='Category',
                                       values='Title',
                                       aggfunc='count').fillna(0).astype(int)
paises_categoria['Total'] = paises_categoria.sum(axis=1)
paises_categoria = paises_categoria.sort_values(by='Total', ascending=False)

#filtrando pelos 10 primeiros resultados
top_paises = paises_categoria.head(10)

#criação do grafico e definição de elementos para os graficos, para visualização dos dados
top_paises[['Movie','TV Show']].plot(kind='barh', stacked = True ,figsize=(20,10))
plt.title('Top 10 paises com mais filmes e series na netflix')
plt.ylabel('quantidade de titulos')
plt.xlabel('pais')
plt.xticks(rotation=45)
plt.legend(title='Categoria')
plt.gca().invert_yaxis()

#salvar para portfolio
plt.savefig('outputs/figures/FilmesVsSeries_porPais.png', dpi=300, bbox_inches='tight')
plt.show()

