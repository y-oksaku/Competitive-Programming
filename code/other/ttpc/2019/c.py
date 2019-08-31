import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N, X = map(int, input().split())
    A_ = list(map(int, input().split()))

    A = list(filter(lambda x: x >= 0, A_))

    B = X
    for a in A:
        B ^= a

    if len(A) == N and B != 0:
        print('-1')
        return

    ans = []
    if B <= X:
        for a in A_:
            if a == -1:
                ans.append(B)
                B = 0
            else:
                ans.append(a)
    else:
        if len(A) + 2 > N:
            print('-1')
            return

        maxDigit = B.bit_length()
        C = (1 << (maxDigit - 1))
        B ^= C
        if C > X or B > X:
            print('-1')
            return

        ans = []
        for a in A_:
            if a == -1:
                if C == 0:
                    ans.append(B)
                    B = 0
                else:
                    ans.append(C)
                    C = 0
            else:
                ans.append(a)

    print(*ans)

sol()