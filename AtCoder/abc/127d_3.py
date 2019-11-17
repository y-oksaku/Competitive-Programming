from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))

cntA = Counter(A)
for _ in range(M):
    B, C = map(int, input().split())
    cntA[C] += B

ans = 0
for val, cnt in sorted(cntA.items(), reverse=True):
    ans += val * min(N, cnt)
    N -= cnt
    if N <= 0:
        break
print(ans)