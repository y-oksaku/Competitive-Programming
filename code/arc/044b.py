import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N = int(input())
    A = list(map(int, input().split()))

    countA = Counter(A)

    if A[0] != 0:
        print(0)
        return

    ans = 1
    for a, count in countA.items():
        if a == 0:
            if count > 1:
                print(0)
                return
            continue
        if countA[a - 1] == 0:
            print(0)
            return

        minDist = pow(pow(2, countA[a - 1], MOD) - 1, count, MOD)
        sameDist = pow(2, count * (count - 1) // 2, MOD)
        ans = (ans * sameDist % MOD) * minDist % MOD

    print(ans)

sol()