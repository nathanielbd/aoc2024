f = open('input.txt', 'r')
data = [row.strip() for row in f]
class Map:
    def __init__(self, data: list[str]):
        self.data = [[int(char) for char in str_list] for str_list in data]
        self.w = len(data[0])
        self.h = len(data)
    def get_tile(self, x: int, y: int):
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        return Tile(x, y, self.data[y][x])
class Tile:
    def __init__(self, x: int, y: int, h: int):
        self.x = x
        self.y = y
        self.h = h
        self.next_steps = None
    def get_neighbors(self, map: Map):
        return [
            neighbor for neighbor in [
                map.get_tile(self.x-1, self.y),
                map.get_tile(self.x+1, self.y),
                map.get_tile(self.x, self.y-1),
                map.get_tile(self.x, self.y+1)
            ] if neighbor
        ]
    def get_next_steps(self, map: Map = None):
        if self.next_steps == None:
            self.next_steps = [neighbor for neighbor in self.get_neighbors(map) if neighbor.h == self.h + 1]
        return self.next_steps
class Trailhead(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 0)
        self.score = 0
    def get_score(self, map: Map):
        peaks = set()
        def get_peaks_(tile: Tile, map: Map):
            if tile.h == 9:
                peaks.add((tile.x, tile.y))
            else:
                next_steps = tile.get_next_steps(map)
                if len(next_steps) == 0:
                    return
                for t in tile.get_next_steps(map):
                    get_peaks_(t, map)
                return
        get_peaks_(self, map)
        return len(peaks)
map = Map(data)
trailheads = [Trailhead(x, y) for y, row in enumerate(map.data) for x, h in enumerate(row) if h == 0]
print(sum([trailhead.get_score(map) for trailhead in trailheads]))