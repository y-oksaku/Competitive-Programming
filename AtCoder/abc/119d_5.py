from bisect import bisect_left

A, B, Q = map(int, input().split())
INF = 10**18
S = [int(input()) for _ in range(A)] + [INF, INF, -INF, -INF]
T = [int(input()) for _ in range(B)] + [INF, INF, -INF, -INF]

S.sort()
T.sort()

for _ in range(Q):
    x = int(input())

    s = bisect_left(S, x)
    ls = S[s - 1]
    rs = S[s]

    t = bisect_left(T, x)
    lt = T[t - 1]
    rt = T[t]

    ans = min(
        abs(ls - rt) + min(abs(x - ls), abs(x - rt)),
        abs(lt - rs) + min(abs(x - lt), abs(x - rs)),
        max(abs(x - ls), abs(x - lt)),
        max(abs(x - rs), abs(x - rt))
    )

    print(ans)
