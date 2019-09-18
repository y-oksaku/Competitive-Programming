from collections import Counter

N, M = map(int, input().split())
X = list(map(int, input().split()))

modGrp = [[] for _ in range(M)]

for x in X:
    modGrp[x % M].append(x)

ans = len(modGrp[0]) // 2
modGrp[0] = []

if M % 2 == 0:
    ans += len(modGrp[M // 2]) // 2
    modGrp[M // 2] = []

for m in range(1, M // 2 + 1):
    S = modGrp[m]
    T = modGrp[M - m]

    if len(S) < len(T):
        S, T = T, S

    cnt = Counter(S)
    dis = 0
    for c in cnt.values():
        while c >= 2 and len(S) - dis * 2 > len(T):
            dis += 1
            c -= 2
            ans += 1

    ans += min(len(T), len(S) - dis * 2)
    modGrp[m] = []
    modGrp[M - m] = []

print(ans)