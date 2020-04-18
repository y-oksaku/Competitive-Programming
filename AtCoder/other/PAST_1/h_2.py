N = int(input())
INF = 10**18
C = [INF] + list(map(int, input().split()))

allMi = min(C)
oddMi = min(C[1::2])
M = len(C[1::2])

Q = int(input())
ans = 0
oddD = 0
allD = 0

for _ in range(Q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        _, x, a = query
        D = allD + (oddD if x % 2 else 0)

        if C[x] - D >= a:
            ans += a
            C[x] -= a
            allMi = min(allMi, C[x])
            if x % 2:
                oddD = min(oddD, C[x])

    if query[0] == 2:
        a = query[1]
        if oddMi - allD - oddD >= a:
            ans += a * M
            oddD += a

    if query[0] == 3:
        a = query[1]
        if min(allMi - allD, oddMi - allD - oddD) >= a:
            ans += a * N
            allD += a

print(ans)
