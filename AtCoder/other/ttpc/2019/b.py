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
    N = int(input())

    ans = []

    for _ in range(N):
        s = input().rstrip()

        okyo = []
        ech = []

        for i in range(len(s)):
            if i + 4 <= len(s):
                if 'okyo' == s[i: i + 4]:
                    okyo.append(i)
            if i + 3 <= len(s):
                if 'ech' == s[i: i + 3]:
                    ech.append(i)

        if okyo and ech:
            if min(okyo) < max(ech):
                ans.append('Yes')
            else:
                ans.append('No')
        else:
            ans.append('No')

    print(*ans, sep='\n')

sol()