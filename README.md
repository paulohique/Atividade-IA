# Análise de Clusters com K-Means e Clustering Hierárquico  

Este projeto aplica técnicas de agrupamento (**K-Means** e **Agglomerative Clustering**) em um conjunto de dados de clientes atacadistas, utilizando a biblioteca **Python** e ferramentas como **Pandas**, **Scikit-learn**, **Seaborn** e **Matplotlib**. O objetivo é identificar grupos de clientes com características semelhantes para uma análise mais aprofundada.

---

## Sobre o Projeto  

O projeto realiza a análise de clusters de dados relacionados ao consumo de produtos por clientes. Ele abrange todo o fluxo de trabalho de agrupamento, incluindo:  
1. **Carregamento e preparação de dados**  
2. **Normalização e padronização dos dados**  
3. **Identificação do número ideal de clusters** usando o método do cotovelo  
4. **Aplicação de algoritmos de clustering**  
5. **Visualização dos clusters em 2D**  
6. **Análise dos clusters**  

---

## Conjunto de Dados  

O conjunto de dados utilizado contém informações sobre o consumo de seis categorias de produtos:  
- **Fresh**  
- **Milk**  
- **Grocery**  
- **Frozen**  
- **Detergents_Paper**  
- **Delicassen**  

### **Pré-processamento**  
Os dados foram padronizados utilizando o **StandardScaler** para garantir que todas as variáveis tenham a mesma escala antes da aplicação dos algoritmos.

---

## Métodos Aplicados  

### **K-Means Clustering**  
O algoritmo K-Means agrupa os dados em clusters, minimizando a soma dos quadrados das distâncias entre os pontos de dados e seus respectivos centros.  
- O número ideal de clusters foi determinado usando o **método do cotovelo**.  

### **Agglomerative Clustering**  
O agrupamento hierárquico cria uma estrutura de clusters baseada em similaridades, usando a métrica **euclidiana** e o método de ligação **Ward**.

### **Redução de Dimensionalidade com PCA**  
A técnica de Análise de Componentes Principais (PCA) foi usada para reduzir os dados para 2 dimensões, facilitando a visualização gráfica dos clusters.

---

## Visualizações  

- **Gráfico do Cotovelo**  
  Utilizado para identificar o número ideal de clusters no K-Means.  

- **Clusters em 2D**  
  Representação dos clusters gerados por ambos os algoritmos após redução de dimensionalidade.  

- **Médias das características por cluster**  
  Gráficos de barras que mostram as médias das variáveis para cada cluster, auxiliando na interpretação e diferenciação dos grupos.

---

