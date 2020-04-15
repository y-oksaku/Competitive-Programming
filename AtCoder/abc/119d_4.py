from bisect import bisect_right, bisect_left
A, B, Q = map(int, input().split())
INF = 10**18

S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]

for _ in range(Q):
    x = int(input())

    lS, lT = S[bisect_right(S, x) - 1], T[bisect_right(T, x) - 1]
    rS, rT = S[bisect_left(S, x)], T[bisect_left(T, x)]

    ans = min(
        abs(lS - lT) + (x - max(lS, lT)),
        abs(rS - rT) + (min(rS, rT) - x),
        (rT - lS) + min(x - lS, rT - x),
        (rS - lT) + min(x - lT, rS - x)
    )

    print(ans)
