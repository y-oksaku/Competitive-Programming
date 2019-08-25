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

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            digit = 0
            while (i & (1 << digit)) == (j & (1 << digit)):
                digit += 1
            print('{} '.format(digit + 1), end='')
        print('')

sol()