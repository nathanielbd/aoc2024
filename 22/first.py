f = open('input.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

def get_secret_n(n: int, iters: int):
    def mix(n: int, mixer: int):
        return n ^ mixer
    def prune(n: int):
        return n & (2**24-1)
    for _ in range(iters):
        n = prune(mix(n, n << 6))
        n = prune(mix(n, n >> 5))
        n = prune(mix(n, n << 11))
    return n

print(sum([get_secret_n(int(row), 2000) for row in data]))