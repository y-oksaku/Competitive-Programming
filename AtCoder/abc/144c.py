import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

# 約数の全列挙
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors.sort(reverse=True)  # ソート
    return divisors

def sol():
    N = int(input())

    divs = divisors(N)
    ans = INF
    for d in divs:
        M = N // d
        ans = min(ans, M - 1 + d - 1)

    print(ans)

sol()