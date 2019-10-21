from heapq import heappush, heappop

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
V = set()

que = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
V.add((0, 0, 0))
ans = []
for _ in range(K):
    val, a, b, c = heappop(que)
    ans.append(-val)

    for x, y, z in [(0, 0, 1), (0, 1, 0), (1, 0, 0)]:
        x = min(a + x, X - 1)
        y = min(b + y, Y - 1)
        z = min(c + z, Z - 1)
        if not (x, y, z) in V:
            heappush(que, (-(A[x] + B[y] + C[z]), x, y, z))
            V.add((x, y, z))

print(*ans, sep='\n')