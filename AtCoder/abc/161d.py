from heapq import heappop, heappush, heapify
K = int(input())
M = K

que = list(range(1, 10))
V = set()
heapify(que)

while M + 100 >= 0:
    top = heappop(que)
    if top in V:
        continue
    V.add(top)
    M -= 1

    top = str(top)
    L = int(top[0])
    R = int(top[-1])

    for i in (L - 1, L, L + 1):
        if 1 <= i <= 9:
            heappush(que, int(str(i) + top))
    for i in (R - 1, R, R + 1):
        if 0 <= i <= 9:
            heappush(que, int(top + str(i)))

V = [int(d) for d in V]
V.sort()
print(V[K - 1])
