from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7
A.sort(reverse=True)

ans = 1
B = deque(A)

if K % 2 == 1:
    ans *= B.popleft()

for _ in range(K // 2):
    l = B[0] * B[1]
    r = B[-1] * B[-2]
    if l >= r:
        ans *= B.popleft() * B.popleft()
    else:
        ans *= B.pop() * B.pop()
    ans = ans % MOD - (MOD if ans < 0 else 0)

if ans < 0:
    ans = 1
    for a in A[:K]:
        ans *= a
        ans %= MOD

print(ans % MOD)
