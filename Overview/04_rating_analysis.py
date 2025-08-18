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

#plotando a janela onde vai ficar o grafico
plt.figure(figsize=(12,8))

#primeiro objeto do grafico
rating_counts = netflix['Rating'].value_counts().sort_values(ascending=False)

#grafico em barras horizontais
rating_counts.plot(kind='barh',color='mediumpurple', title='Distribution of Ratings')
plt.xlabel('Numero de titulos')
plt.ylabel('Rating')
plt.grid(axis='x', linestyle='--', alpha=0.7)

for i, v in enumerate(rating_counts):
    plt.text(v+10,i, str(v),va = 'center', fontweight='bold')


#salvar para portfolio
plt.savefig('outputs/figures/DistribuiçãoDeFaixasEtarias.png', dpi=300, bbox_inches='tight')
plt.show()
