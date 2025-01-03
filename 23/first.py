import networkx as nx

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

G = nx.Graph()
G.add_edges_from(row.split('-') for row in data)
print(sum(len(clique) == 3 and any(computer.startswith('t') for computer in clique) for clique in nx.enumerate_all_cliques(G)))