import heapq

def sol():
    N = int(input())
    A = list(map(int, input().split()))

    hq = []
    for a in A:
        heapq.heappush(hq, a)

    while len(hq) > 1:
        x = heapq.heappop(hq)
        y = heapq.heappop(hq)
        new = (x + y) / 2
        heapq.heappush(hq, new)

    ans = heapq.heappop(hq)
    print(ans)


sol()