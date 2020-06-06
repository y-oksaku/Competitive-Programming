N = int(input())

for i in range(N - 1):
    row = []
    for j in range(i + 1, N):
        d = 0
        while (i & (1 << d)) == (j & (1 << d)):
            d += 1
        row.append(d + 1)
    print(*row)
