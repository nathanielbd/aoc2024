from functools import cache

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']
PATTERNS = data[0].split(', ')
designs = data[1:]

@cache
def num_possible(design: str):
    if len(design) == 0:
        return 1
    return sum(
        num_possible(design[len(pattern):])
        for pattern in PATTERNS
        if design[:len(pattern)] == pattern
    )
print(sum([num_possible(design) for design in designs]))
