N = int(input())
INF = float('inf')

L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

maxL = max(L)
minR = min(R)

LR = [(minR - l + 1, r - maxL + 1) for l, r in zip(L, R)]
LR.sort()

ans = 0
S = INF
# aは増加
for (_, b), (a, _) in zip(LR, LR[1:]):
    S = min(S, b)
    ans = max(ans, a + S)

# minLとmaxRを一緒にする
for l, r in zip(L, R):
    now = r - l + 1
    now += max(0, minR - maxL + 1)
    ans = max(ans, now)

print(ans)