
#imports necessarios
import pandas as pd
from matplotlib import pyplot as plt

#carrega o dataset original
csv_url = "https://raw.githubusercontent.com/luscasdsz/ProjetoNetflixDataset/main/data/Netflix%20Dataset.csv"
csv = pd.read_csv(csv_url, sep=',',encoding='utf-8')

#processamento de dados
#tratamento de nulos
csv['Country'] = csv['Country'].fillna('unknown')
csv['Rating'] = csv['Rating'].fillna('unrated')

#criação do objeto final
netflix = csv[['Category','Title','Country','Release_Date','Rating','Duration','Type']]

#analise de filmes vs series no catalogo da netflix
#Produção do grafico em barras
counts = netflix['Category'].value_counts()
plt.figure(figsize=(6,4))
counts.plot(kind='bar', color=['Skyblue','salmon'], title = 'Filmes vs Series na netflix')
plt.ylabel('Número de títulos')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(counts):
    plt.text(i, v + 50, str(v), ha='center', fontweight='bold')


#salvar para portfolio
plt.savefig('outputs/figures/overview_filmes_vs_series.png', dpi=300, bbox_inches='tight')
plt.show()