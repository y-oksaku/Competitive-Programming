import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def search(n):  # 一番下の桁から
    if n == 0:
        return 0

    q, r = divmod(n, 10)
    ret = 0
    if r > 1:
        ret += 1

    ret += str(q).count('1') * r
    ret += search(q) * 10
    ret += q
    return ret

def sol():
    N = int(input())

    ans = search(N + 1)
    print(ans)


sol()