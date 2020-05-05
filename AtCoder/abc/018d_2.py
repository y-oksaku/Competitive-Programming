from itertools import combinations

def sol():
    N, M, P, Q, R = map(int, input().split())

    YZ = [[] for _ in range(N)]
    for _ in range(R):
        x, y, z = map(int, input().split())
        YZ[x - 1].append((y - 1, z))

    ans = 0
    for A in combinations(range(N), r=P):
        val = [0] * M
        for a in A:
            for y, z in YZ[a]:
                val[y] += z
        val.sort(reverse=True)
        ans = max(ans, sum(val[:Q]))
    print(ans)

sol()