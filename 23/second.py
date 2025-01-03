import networkx as nx

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

G = nx.Graph()
G.add_edges_from(row.split('-') for row in data)
print(','.join(sorted(nx.approximation.max_clique(G))))