from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [a % M for a in A]

accA = [0] * (N + 1)
for i, a in enumerate(A, start=1):
    accA[i] = accA[i - 1] + a

cnt = defaultdict(int)
for a in accA:
    cnt[a % M] += 1

def ncr(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    ret = 1
    for i in range(n, n - r, -1):
        ret *= i
    for i in range(1, r + 1):
        ret //= i
    return ret

ans = 0
for c in cnt.values():
    ans += ncr(c, 2)

print(ans)