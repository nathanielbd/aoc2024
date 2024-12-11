f = open('input.txt', 'r')
data = [row.strip() for row in f]
diskmap = data[0]
def get_filler_file(file_blocks: list[int], file_ids: list[int]):
    while len(file_blocks) > 0:
        file_length = file_blocks.pop()
        file_id = file_ids.pop()
        for _ in range(file_length):
            yield file_id
def get_file(diskmap: str):
    file_blocks = [int(digit) for digit in diskmap[::2]]
    file_ids = list(range(len(file_blocks)))
    filler_file_gen = get_filler_file(file_blocks, file_ids)
    for idx, digit in enumerate(diskmap):
        if idx % 2 == 0:
            for _ in range(int(digit)):
                yield idx // 2
        if idx % 2 == 1:
            for _ in range(int(digit)):
                yield next(filler_file_gen)
length = sum([int(digit) for digit in diskmap[::2]])
print(sum([idx*file_id for idx, file_id in zip(range(length), get_file(diskmap))]))