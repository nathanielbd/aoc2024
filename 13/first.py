import numpy as np

A_PRICE = 3
B_PRICE = 1

f = open('example.txt', 'r')
data = [row.strip() for row in f if row.strip() != '']

total = 0

for button_a, button_b, prize in zip(data[::3], data[1::3], data[2::3]):
    def parse_info(line: str, sep: str):
        return int(line.split(sep)[1].split(',')[0]), int(line.split(sep)[2])
    a_x, a_y = parse_info(button_a, '+')
    b_x, b_y = parse_info(button_b, '+')
    A = np.array([[a_x, b_x],
                  [a_y, b_y]])
    p_x, p_y = parse_info(prize, '=')
    b = np.array([p_x,
                  p_y])
    sol = np.linalg.solve(A, b)
    if all([np.isclose(x, int(x)) for x in sol]):
        total += sol[0]*A_PRICE + sol[1]*B_PRICE
print(int(total))