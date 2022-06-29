import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st


df= pd.read_csv("ChG-Miner_miner-chem-gene.tsv", sep='\t')

# print the first 10 records

print(df.head(10))

m = df.pivot(*df).fillna(0).rename_axis(index=None,columns=None)
#final = m.reindex(index=m.index[m.index.map(dic1)],columns=m.columns[m.columns.map(dic2)])

G = nx.from_pandas_edgelist(df, "#Drug", "Gene")

r = nx.pagerank(G, alpha = 0.9)

print(G)
nx.draw_networkx(G)
nx.draw(G)
nx.edges(G)
#plt.show()

# plt.show()
plt.savefig("Graph.png", format = "PNG")