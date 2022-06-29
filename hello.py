# importing the "tarfile" module
import pypathway
import networkx as nx
import matplotlib.pyplot as plt
import gzip
import csv


with gzip.open('DG-AssocMiner_miner-disease-gene.tsv.gz', 'rb') as f:
    data = f.read().decode()



    with open(data) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
            print(line)
    # print('--- data ---')
    # print(data)
    # print('---')

    tsv_reader = csv.reader(data, delimiter="\t")

    number_of_lines = 10

    for i in range(number_of_lines):
        row = next(tsv_reader)
        print(i, row)


def data_extraction(data):
    # Here, data loading will be done through a context manager
    with open(data, 'r', encoding='utf8') as rf:
        # transform file into string and split along new line
        filelines = rf.read().split("\n")

        # new line will be created at tab spaces
        filedata = [line.split("\t") for line in filelines]

        # picks the header
        fileheader = filedata[0]

        # header gets deleted
        filedata = filedata[1:]

    # return header and data
    return fileheader, filedata


# load data in from file
headerofnode, data_ofnode = data_extraction(data)

Graph = nxnas.Graph()

# graph gets data of node added to it
for nxnode in data_ofnode:
    # sequentially adding id, name, chinese name, and index year
    Graph.add_node(int(nxnode[0]), pname=nxnode[1], chinese_name=nxnode[2], year_inindex=int(nxnode[3]))

#  graph gets data of edge added to it
for nxedge in data_ofedge:
    # sequentially adding node 1, node 2, kin, and label
    Graph.add_edge(int(nxedge[0]), int(nxedge[1]), nxkin=nxedge[2], nxlabel=nxedge[3])

# Data metrics for the graph
degree_centrality = nxnas.degree_centrality(Graph)
closeness_centrality = nxnas.closeness_centrality(Graph)
betweenness_centrality = nxnas.betweenness_centrality(Graph)

# The process of depicting the graph
nxnas.draw_spring(Graph)
myplot.show()



