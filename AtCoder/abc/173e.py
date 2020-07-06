from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

P = [a for a in A if a >= 0]
N = [a for a in A if a < 0]

def canPositive():
    for i in range(0, len(N) + 1, 2):
        p = K - i
        if p < 0:
            break
        if len(P) >= p:
            return True
    return False

if not canPositive():
    A.sort(key=lambda a: abs(a))
    ans = 1
    for a in A[:K]:
        ans *= a
        ans %= MOD
    print(ans)
    exit()

if not P or not N or len(A) == K:
    A.sort(key=lambda a: abs(a), reverse=True)
    ans = 1
    for a in A[:K]:
        ans *= a
        ans %= MOD
    print(ans)
    exit()

P.sort(key=lambda a: abs(a))
N.sort(key=lambda a: abs(a))
P = deque(P)
N = deque(N)

ans = 1
sign = 1
while K > 0:
    ans %= MOD
    if ans == 0:
        break
    if K == 1:
        if sign < 0:
            ans *= N.pop()
        else:
            ans *= P.pop()
        break

    if len(P) >= 2 and len(N) >= 2:
        p = P[-1] * P[-2]
        n = N[-1] * N[-2]
        if p > n:
            ans *= P.pop()
            K -= 1
        else:
            ans *= N.pop() * N.pop()
            K -= 2
        continue
    if len(P) <= 1 or len(N) <= 1:
        if len(N) == 0:
            ans *= P.pop()
            K -= 1
            continue

        if len(P) == 0:
            ans *= N.pop()
            K -= 1
            sign *= -1
            continue

        if len(N) == 1:
            n = N.pop()
            if sign < 0:
                ans *= n
                K -= 1
                sign *= -1
            continue

        if len(P) == 1:
            p = P.pop()
            if K % 2 == 1 and sign > 0 or K % 2 == 0 and sign < 0:
                ans *= p
                K -= 1
            continue

print(ans % MOD)
