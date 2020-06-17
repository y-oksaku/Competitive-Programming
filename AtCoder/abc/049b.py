H, W = map(int, input().split())
C = [input() for _ in range(H)]

for h in range(H * 2):
    ans = []
    for w in range(W):
        ans.append(C[h // 2][w])
    print(''.join(ans))
