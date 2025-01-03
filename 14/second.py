from statistics import variance

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

HEIGHT = 103
WIDTH = 101

class Robot:
    def __init__(self, row: str):
        p, v = row.split(' ')
        self.p = eval(f"({p.split('=')[1]})")
        self.v = eval(f"({v.split('=')[1]})")
    
    def after_secs(self, secs: int):
        disp = tuple(vs*secs for vs in self.v)
        return (
            (self.p[0] + disp[0]) % WIDTH,
            (self.p[1] + disp[1]) % HEIGHT
        )
    
class Map:
    def __init__(self, ps: list[tuple[int, int]]):
        self.ps = ps

    def __str__(self):
        return ''.join(
            ''.join(
                '#' if (x, y) in self.ps else '.'
                for x in range(WIDTH)
            ) + '\n'
            for y in range(HEIGHT)
        )
    
    def get_xvar(self):
        xs = [x for x, _ in ps]
        return variance(xs)

    def get_yvar(self):
        ys = [y for _, y in ps]
        return variance(ys)

robots = [Robot(row) for row in data]

min_xvar = float('inf')
min_yvar = float('inf')
argmin_xvar = 0
argmin_yvar = 0
for i in range(max(WIDTH, HEIGHT)):
    ps = [robot.after_secs(i) for robot in robots]
    map = Map(ps)
    xvar = map.get_xvar()
    if xvar < min_xvar:
        min_xvar = xvar
        argmin_xvar = i
    yvar = map.get_yvar()
    if yvar < min_yvar:
        min_yvar = yvar
        argmin_yvar = i

def bezout(a, b):
    a, b = min(a, b), max(a, b)
    d = [b//a]
    e = [a, b%a]
    while e[-1] != 0:
        d.append(e[-2]//e[-1])
        e.append(e[-2]%e[-1])
    z = [(0, 1), (1, -d[0])]
    for i in range(1, len(d)-1):
        x = z[i-1][0] - d[i]*z[i][0]
        y = z[i-1][1] - d[i]*z[i][1]
        z.append((x,y))
    return z[-1][1], z[-1][0]

u, v = bezout(WIDTH, HEIGHT)
j = (argmin_yvar*u*WIDTH + argmin_xvar*v*HEIGHT) % (WIDTH*HEIGHT)

print(j) 
print(Map([robot.after_secs(j) for robot in robots]))