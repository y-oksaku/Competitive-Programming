from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**18
L = [INF] * N

ans = []
for a in A:
    i = bisect_right(L, -a)
    if i == N:
        ans.append(-1)
        continue
    ans.append(i + 1)
    L[i] = -a

print(*ans, sep='\n')