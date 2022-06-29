import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("Static_PPIN_HAZBUN.txt", sep="\s+", names=["column1", "column2", "WEIGHT"])
print(df)
G = nx.Graph()
G = nx.from_pandas_edgelist(df, "column1", "column2")

pr = nx.pagerank(G, alpha = 0.9)
print(pr)
print(G)
nx.draw_networkx(G)
nx.draw(G)

nx.edges(G)
plt.show()

st.table(df)


#def my_own_function(df):
    #iterative Matrix Multiplikation
    #dann zeigen was dabei rausgekommen ist!





