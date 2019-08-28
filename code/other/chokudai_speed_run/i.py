import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    item = [0] * N

    for i in range(N):
        A, B = map(int, input().split())
        item[i] = (A, B)

    now = set(range(N))
    while len(now) > 1:
        nx = set([])
        while len(now) > 1:
            i = now.pop()
            j = now.pop()
            A1, B1 = item[i]
            A2, B2 = item[j]
            I = (A1 + B2 - 1) // B2
            J = (A2 + B1 - 1) // B1
            if I > J:
                nx.add(i)
            else:
                nx.add(j)
        else:
            if len(now) == 1:
                nx.add(now.pop())
        now = nx

    ans = now.pop()
    A, B = item[ans]
    for j, (a, b) in enumerate(item):
        if ans == j:
            continue
        I = (A + b - 1) // b
        J = (a + B - 1) // B
        if I > J:
            continue
        else:
            print(-1)
            return
    print(ans + 1)


sol()