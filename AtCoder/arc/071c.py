from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

V = Counter(S[0])
for s in S:
    cntS = Counter(s)
    for t in S[0]:
        V[t] = min(V[t], cntS[t])

ans = []
for s in sorted(V.keys()):
    ans += [s] * V[s]
print(''.join(ans))