H, W, D = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

aToHW = {}
for h in range(H):
    for w, a in enumerate(A[h]):
        aToHW[a] = (h, w)

cnt = [-1] * (H * W + 1)
for start in range(1, H * W + 1)[:: -1]:
    c = 0
    for now in range(start, H * W + 1, D):
        if now + D > H * W:
            break
        if cnt[now] >= 0:
            c += cnt[now]
            break

        nH, nW = aToHW[now]
        tH, tW = aToHW[now + D]
        c += abs(nH - tH) + abs(nW - tW)
    cnt[start] = c

Q = int(input())
ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    ans.append(cnt[L] - cnt[R])

print(*ans, sep='\n')