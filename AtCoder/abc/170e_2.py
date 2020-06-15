import sys
input = sys.stdin.buffer.readline
from heapq import heappush, heappop
from collections import Counter

class HeapSet:
    def __init__(self):
        self.minQue = []
        self.maxQue = []
        self.counter = Counter()

    def insert(self, x):
        heappush(self.minQue, x)
        heappush(self.maxQue, -x)
        self.counter[x] += 1

    def erase(self, x):
        self.counter[x] -= 1

    def max(self):
        while self.maxQue and self.counter[-self.maxQue[0]] == 0:
            heappop(self.maxQue)
        return -self.maxQue[0] if self.maxQue else None

    def min(self):
        while self.minQue and self.counter[self.minQue[0]] == 0:
            heappop(self.minQue)
        return self.minQue[0] if self.minQue else None

def sol():
    N, Q = map(int, input().split())
    iToNo = [-1] * N
    iToRate = [0] * N
    M = 2 * 10**5 + 10000

    A = [HeapSet() for _ in range(M)]

    for i in range(N):
        rate, no = map(int, input().split())
        no -= 1
        iToNo[i] = no
        iToRate[i] = rate

        A[no].insert(rate)

    rates = HeapSet()
    for i in range(M):
        if A[i].max():
            rates.insert(A[i].max())

    ans = []
    for _ in range(Q):
        i, to = map(int, input().split())
        i -= 1
        to -= 1

        fr = iToNo[i]
        rate = iToRate[i]
        iToNo[i] = to

        rates.erase(A[fr].max())
        if A[to].max():
            rates.erase(A[to].max())

        A[fr].erase(rate)
        A[to].insert(rate)

        if A[fr].max():
            rates.insert(A[fr].max())
        rates.insert(A[to].max())

        ans.append(rates.min())

    print(*ans, sep='\n')

sol()