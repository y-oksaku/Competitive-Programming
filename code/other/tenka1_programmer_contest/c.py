N = int(input())

for a in range(1, 3501):
    for b in range(1, 3501):
        if 4 * a * b - N * (a + b) == 0:
            continue
        c = N * a * b / (4 * a * b - N * (a + b))
        if c.is_integer() and c > 0:
            print(*list(map(int, [a, b, c])))
            exit()