W, H = map(int, input().split())

cost = [(int(input()), i, 'r') for i in range(W)] + [(int(input()), i, 'c') for i in range(H)]

cost.sort()
row = H + 1
col = W + 1
ans = 0

for c, i, t in cost:
    if t == 'r':
        ans += max(0, row) * c
        col -= 1
    else:
        ans += max(0, col) * c
        row -= 1

print(ans)