import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    N, L = map(int, input().split())

    amida = [0] * L
    for i in range(L):
        line = input().strip()
        amida[i] = line

    goal = 0
    line = input()
    for i, l in enumerate(line):
        if l == 'o':
            goal = i

    for l in amida[:: -1]:
        if goal > 1:
            if l[goal - 1] == '-':
                goal -= 2
                continue
        if goal < N * 2 - 2:
            if l[goal + 1] == '-':
                goal += 2
                continue

    print(goal // 2 + 1)

sol()