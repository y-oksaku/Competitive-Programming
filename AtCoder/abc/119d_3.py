from bisect import bisect_left, bisect_right

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)] + [float('inf'), -float('inf')]
T = [int(input()) for _ in range(B)] + [float('inf'), -float('inf')]

S.sort()
T.sort()

ans = []
for _ in range(Q):
    x = int(input())

    midS = bisect_right(S, x)
    midT = bisect_right(T, x)

    lS = S[midS - 1]
    rS = S[midS]
    lT = T[midT - 1]
    rT = T[midT]

    dist = min(
        max(rS, rT) - x,
        x - min(lS, lT),
        abs(rS - lT) + min(rS - x, x - lT),
        abs(rT - lS) + min(rT - x, x - lS)
    )

    ans.append(dist)

print(*ans, sep='\n')