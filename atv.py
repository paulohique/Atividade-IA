# Importar Bibliotecas
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
df = pd.read_csv("Wholesale customers data.csv")

# Seleção das colunas de interesse para o agrupamento
data = df[['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']]

# Padronizar os dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Determinando o número ótimo de clusters usando o método do cotovelo
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)

# Plot do gráfico do cotovelo
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title("Método do Cotovelo")
plt.xlabel("Número de Clusters")
plt.ylabel("WCSS")
plt.grid()
plt.show()

# Aplicando o K-Means com o número de clusters ótimo (exemplo com 4 clusters)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
kmeans_clusters = kmeans.fit_predict(data_scaled)

# Adicionando os clusters ao DataFrame original
df['KMeans_Cluster'] = kmeans_clusters

# Aplicando o AgglomerativeClustering com o argumento corrigido
hierarchical = AgglomerativeClustering(n_clusters=4, metric='euclidean', linkage='ward')
hierarchical_clusters = hierarchical.fit_predict(data_scaled)

# Adicionando os clusters ao DataFrame original
df['Hierarchical_Cluster'] = hierarchical_clusters

# Redução de dimensionalidade para 2D
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Plot dos clusters do K-Means
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=df['KMeans_Cluster'], palette='viridis')
plt.title("Clusters do K-Means")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.legend(title='Clusters')
plt.grid()

# Plot dos clusters hierárquicos
plt.subplot(1, 2, 2)
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=df['Hierarchical_Cluster'], palette='viridis')
plt.title("Clusters Hierárquicos")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.legend(title='Clusters')
plt.grid()

plt.tight_layout()
plt.show()

# Analisando as características médias de cada cluster
cluster_analysis_kmeans = df.groupby('KMeans_Cluster')[['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']].mean()
cluster_analysis_hierarchical = df.groupby('Hierarchical_Cluster')[['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']].mean()

print("Análise de Cluster - K-Means:")
print(cluster_analysis_kmeans)

print("\nAnálise de Cluster - Hierarchical:")
print(cluster_analysis_hierarchical)

# Visualização das médias em um gráfico
cluster_analysis_kmeans.plot(kind='bar', figsize=(12, 6))
plt.title('Médias das Características por Cluster (K-Means)')
plt.ylabel('Média')
plt.xlabel('Cluster')
plt.xticks(rotation=0)
plt.grid()
plt.show()

cluster_analysis_hierarchical.plot(kind='bar', figsize=(12, 6))
plt.title('Médias das Características por Cluster (Hierarchical)')
plt.ylabel('Média')
plt.xlabel('Cluster')
plt.xticks(rotation=0)
plt.grid()
plt.show()
