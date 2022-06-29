import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("Dynamic_PPIN.txt", sep=",", names=["column1", "column2", "time", "weight"])
print(df)

# unweighted Graph
G = nx.Graph()
G = nx.from_pandas_edgelist(df, "column1", "column2")
weights = [i * 5 for i in df['weight'].tolist()]
pos = nx.spring_layout(G, k=0.9)
nx.draw_networkx_edges(G, pos, edge_color='#06D6A0', arrowsize=22, width=weights)
nx.draw_networkx_nodes(G, pos,node_color='#EF476F', node_size=100)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_color='black')
plt.gca().margins(0.1, 0.1)
plt.show()

# weighted Graph
G_weighted = nx.from_pandas_edgelist(df, 'column1', 'column2', create_using=nx.DiGraph, edge_attr='weight')

#Normal default pagerank for the undirected graph
pr = nx.pagerank(G)
print(pr)
df_pagerank = pd.DataFrame.from_dict(pr, orient="index", columns=['A'])
print(df_pagerank.sort_values(by=['A'], ascending = False))

#Personalized Page Rank with unweighted graph
pr_personalized = nx.pagerank(G, personalization={16 : 0.5})
print(pr_personalized)
df_pagerank = pd.DataFrame.from_dict(pr_personalized, orient="index", columns=['A'])
print(df_pagerank.sort_values(by=['A'], ascending = False))

print(G)
#nx.draw_networkx(G)
#nx.draw(G)

#nx.edges(G)
#plt.show()

#st.table(df)