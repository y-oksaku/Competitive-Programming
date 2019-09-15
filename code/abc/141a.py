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
    S = input()
    if S[0] == 'S':
        print('Cloudy')
    elif S[0] == 'C':
        print('Rainy')
    else:
        print('Sunny')

sol()