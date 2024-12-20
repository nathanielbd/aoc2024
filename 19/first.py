from functools import cache

f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']
PATTERNS = data[0].split(', ')
designs = data[1:]

@cache
def is_possible(design: str):
    if len(design) == 0:
        return True
    return any(
        is_possible(design[len(pattern):])
        for pattern in PATTERNS
        if design[:len(pattern)] == pattern
    )
print(sum([is_possible(design) for design in designs]))
