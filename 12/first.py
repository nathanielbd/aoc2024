f = open('input.txt', 'r')
data = [row.strip() for row in f]
class Map:
    def __init__(self, data: list[str]):
        self.data = [[char for char in str_list] for str_list in data]
        self.w = len(data[0])
        self.h = len(data)
        self.regions: list[Region] = []
        self.assigned: set[tuple[int, int]] = set()
    def get_plot(self, x: int, y: int):
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return None
        return Plot(x, y, self.data[y][x])
    def assign_plot(self, x: int, y: int):
        def accumulate_region(x: int, y: int, region: Region = None):
            plot = self.get_plot(x, y)
            region_mates = plot.get_region_mates(self)
            n = len(region_mates)
            self.assigned.add((x, y))
            if region == None:
                region = Region(plot, n)
            for region_mate in region_mates:
                if (region_mate.x, region_mate.y) not in self.assigned:
                    self.assigned.add((region_mate.x, region_mate.y))
                    region.add(region_mate, len(region_mate.get_region_mates(self)))
                    region = accumulate_region(region_mate.x, region_mate.y, region)
            return region
        if (x, y) not in self.assigned:
            region = accumulate_region(x, y)
            self.regions.append(region)
class Plot:
    def __init__(self, x: int, y: int, plant: str):
        self.x = x
        self.y = y
        self.plant = plant
        self.region: Region = None
    def get_neighbors(self, map: Map):
        return [
            neighbor for neighbor in [
                map.get_plot(self.x-1, self.y),
                map.get_plot(self.x+1, self.y),
                map.get_plot(self.x, self.y-1),
                map.get_plot(self.x, self.y+1)
            ] if neighbor
        ]
    def get_region_mates(self, map: Map):
        return [neighbor for neighbor in self.get_neighbors(map) if neighbor.plant == self.plant]
class Region:
    def __init__(self, plot: Plot, region_mates: int):
        self.plots = [plot]
        self.perimeter = 4 - region_mates
        self.area = 1
    def add(self, plot: Plot, region_mates: int):
        plot.region = self
        self.plots.append(plot)
        self.area += 1
        self.perimeter += 4 - region_mates
    def get_price(self):
        return self.perimeter * self.area
map = Map(data)
for x in range(map.w):
    for y in range(map.h):
        map.assign_plot(x, y)
print(sum([region.get_price() for region in map.regions]))