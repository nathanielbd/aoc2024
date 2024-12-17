import networkx as nx

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

class Map:
    def __init__(self, data: list[str]):
        self.data = [[char for char in str_list] for str_list in data]
        self.w = len(data[0])
        self.h = len(data)
        self.tiles = self.get_tiles()
        self.source = self.get_tiles('S')[0]
        self.end = self.get_tiles('E')[0]
        self.tiles = [self.source] + self.tiles + [self.end]

    def get_tiles(self, sep = '.'):
        return [(x, y) for y, row in enumerate(self.data) for x, char in enumerate(row) if char == sep]

map = Map(data)
G = nx.Graph()
G.add_nodes_from([(x, y, 1j**d) for x, y in map.tiles for d in range(4)])
G.add_edges_from([((x, y, 1j**d), (x, y, 1j**(d+1)), {"weight": 1000}) for x, y in map.tiles for d in range(4)])
for y, row in enumerate(map.data):
    for x, char in enumerate(row):
        if y == 0 or y == map.h-1 or x == 0 or x == map.w-1:
            continue
        if map.data[y][x] not in ['S', 'E', '.']:
            continue
        for rot in [1j**d for d in range(4)]:
            adj_node = (x+rot.real, y+rot.imag, rot)
            if G.has_node(adj_node):
                G.add_edge((x, y, rot), adj_node)
print(min([nx.shortest_path_length(G, (*map.source, 1+0j), (*map.end, rot), "weight") for rot in [1j**d for d in range(4)]]))