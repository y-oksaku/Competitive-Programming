from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 10**9 + 7

if len(A) != len(set(A)) or len(B) != len(set(B)):
    print(0)
    exit()

A.sort()
B.sort()
setA = set(A)
setB = set(B)

ans = 1
for i, x in enumerate(range(1, N * M + 1)[:: -1]):
    if x in setA and x in setB:
        continue
    elif x in setA:
        ans *= (M - bisect_left(B, x))
    elif x in setB:
        ans *= (N - bisect_left(A, x))
    else:
        ans *= (M - bisect_left(B, x)) * (N - bisect_left(A, x)) - i
    ans %= MOD

print(ans)