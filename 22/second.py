from collections import defaultdict

f = open('example2.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

BANANAS = defaultdict(int)

def get_price(n: int, iters: int):
    def mix(n: int, mixer: int):
        return n ^ mixer
    def prune(n: int):
        return n & (2**24-1)
    changes = []
    seqs = set()
    for _ in range(iters):
        prev_n = n
        prev_price = prev_n % 10
        n = prune(mix(n, n << 6))
        n = prune(mix(n, n >> 5))
        n = prune(mix(n, n << 11))
        price = n % 10
        changes.append(price - prev_price)
        if len(changes) == 4:
            seq = ','.join(map(str, changes))
            if seq not in seqs:
                seqs.add(seq)
                BANANAS[seq] += price
            changes.pop(0)

for row in data:
    get_price(int(row), 2000)
print(max(BANANAS.values()))