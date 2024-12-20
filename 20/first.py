from collections import Counter
import networkx as nx

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

TRACKS = ['S', 'E', '.']

class Map:
    def __init__(self, data: list[str]):
        self.data = [[char for char in str_list] for str_list in data]
        self.w = len(data[0])
        self.h = len(data)
        self.tiles = self.get_tiles()
        self.source = self.get_tiles('S')[0]
        self.end = self.get_tiles('E')[0]
        self.tiles = [self.source] + self.tiles + [self.end]
        self.walls = self.get_tiles("#")

    def get_tile(self, x: int, y: int):
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        return Tile(x, y, self.data[y][x])

    def get_tiles(self, sep = '.'):
        return [(x, y) for y, row in enumerate(self.data) for x, char in enumerate(row) if char == sep]

class Tile:
    def __init__(self, x: int, y: int, char: str):
        self.x = x
        self.y = y
        self.char = char
    def get_neighbors(self, map: Map):
        return [
            neighbor for neighbor in [
                map.get_tile(self.x-1, self.y),
                map.get_tile(self.x+1, self.y),
                map.get_tile(self.x, self.y-1),
                map.get_tile(self.x, self.y+1)
            ] if neighbor
        ]
    
class Cheat(Tile):
    def __init__(self, wall: tuple[int, int]):
        super().__init__(*wall, '#')

    def get_savings(self, map: Map, g: nx.Graph):
        neighbor_tracks = [
            neighbor for neighbor in self.get_neighbors(map)
            if neighbor.char in TRACKS
        ]
        cheats = [
            (t1, t2) for t1 in neighbor_tracks for t2 in neighbor_tracks
            if t1 != t2
        ]
        return max(nx.shortest_path_length(g, (t1.x, t1.y), (t2.x, t2.y)) - 2 for t1, t2 in cheats) if cheats else 0

map = Map(data)
G = nx.Graph()
G.add_nodes_from(map.tiles)
for node in G:
    G.add_edges_from(
        [
            (node, (neighbor.x, neighbor.y)) 
            for neighbor in map.get_tile(*node).get_neighbors(map) 
            if neighbor.char in TRACKS
        ]
    )
cheats = Counter([Cheat(wall).get_savings(map, G) for wall in map.walls])
print(sum([cheats[key] for key in cheats.keys() if key >= 100]))