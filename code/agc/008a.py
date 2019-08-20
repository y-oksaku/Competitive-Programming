import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    x, y = map(int, input().split())

    a = 0
    if y < x:
        a = abs(x - y) + 2
    else:
        a = abs(x - y)

    ans = min(a, abs(x + y) + 1)
    print(ans)


sol()