from collections import Counter
from math import prod

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

robots = [Robot(row) for row in data]
ps = [robot.after_secs(100) for robot in robots]

def get_quadrant(p: tuple[int, int]):
    x, y = p
    x_margin = WIDTH//2
    y_margin = HEIGHT//2
    left = x < x_margin
    right = x >= WIDTH - x_margin
    up = y < y_margin
    down = y >= HEIGHT - y_margin
    match (left, right, up, down):
        case (False, True, True, False):
            return 1
        case (True, False, True, False):
            return 2
        case (True, False, False, True):
            return 3
        case (False, True, False, True):
            return 4
        case _:
            return 0
        
counts = Counter([get_quadrant(p) for p in ps])
print(prod([counts[x] for x in [1, 2, 3, 4]]))