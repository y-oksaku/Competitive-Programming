ans = []

row = 0
col = 0

for i in range(1, 101)[::-1]:
    if col + 2 * i > 1500:
        col = 0
        row += 200
    ans.append((row + i, col + i))
    col += 2 * i

for x, y in ans[::-1]:
    print(x, y)
