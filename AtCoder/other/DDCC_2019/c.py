H, W, K = map(int, input().split())

chart = [input() for _ in range(H)]

ans = [[-1] * W for _ in range(H)]
now = 1

for h in range(H):
    for w in range(W):
        if chart[h][w] == '#':
            ans[h][w] = now
            for rw in range(w - 1, -1, -1):
                if chart[h][rw] == '#':
                    break
                if ans[h][rw] == -1:
                    ans[h][rw] = now
                else:
                    break
            for rw in range(w + 1, W):
                if chart[h][rw] == '#':
                    break
                if ans[h][rw] == -1:
                    ans[h][rw] = now
                else:
                    break
            now += 1

nonEmpPrev = None
for h, line in enumerate(ans):
    if set(line) == set([-1]):
        if nonEmpPrev != None:
            print(*nonEmpPrev)
        else:
            for n in ans[h + 1:]:
                if set(n) != set([-1]):
                    nonEmpPrev = n
                    break
            print(*nonEmpPrev)
    else:
        print(*line)
        nonEmpPrev = line