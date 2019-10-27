import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

import re

def sol():
    S = input().rstrip()

    num = re.sub(r'[a-zA-Z]', '', S)

    print(num)

sol()