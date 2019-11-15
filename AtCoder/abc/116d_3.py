from collections import defaultdict

N, K = map(int, input().split())
TD = [tuple(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda A: A[1], reverse=True)

A = TD[:K][:: -1]
cnt = defaultdict(int)
V = set()
dSum = 0
for t, d in A:
    dSum += d
    cnt[t] += 1
    V.add(t)

i = 0
ans = dSum + len(V)**2
for t, d in TD[K:]:
    if not t in V:
        while i < K and cnt[A[i][0]] <= 1:
            i += 1
        if i == K:
            break

        dSum = dSum - A[i][1] + d
        V.add(t)
        cnt[A[i][0]] -= 1
        i += 1
        ans = max(ans, dSum + len(V)**2)

print(ans)
