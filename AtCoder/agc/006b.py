import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    N, x = map(int, input().split())

    if x == 1 or x == 2 * N - 1:
        print('No')
    else:
        print('Yes')
        ans = [None] * (2 * N - 1)
        numList = list(range(1, 2 * N))

        for i in range(3):
            ans[N - 2 + i] = x - 1 + i
            numList[x - 2 + i] = None
        if x > N:
            ans[N + 1] = 1
            numList[0] = None
        elif x < N:
            ans[N - 3] = 2 * N - 1
            numList[2 * N - 2] = None

        numList = list(filter(lambda n: n != None, numList))
        now = 0
        for a in ans:
            if a == None:
                print(numList[now])
                now += 1
            else:
                print(a)



sol()