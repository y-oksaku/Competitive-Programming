H, W = map(int, input().split())
atlas = [[False for _ in range(W + 2)] for _ in range(H + 2)]

for h in range(1, H + 1):
    line = input()
    for w in range(1, W + 1):
        if line[w - 1] == '#':
            atlas[h][w] = True

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if atlas[h][w]:
            if atlas[h - 1][w] or atlas[h + 1][w] or atlas[h][w - 1] or atlas[h][w + 1]:
                continue
            print('No')
            exit(0)
print('Yes')