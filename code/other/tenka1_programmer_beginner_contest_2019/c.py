import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    N = int(input())
    S = input().rstrip()

    # すべてを白/黒にするコスト
    ans = min(S.count('.'), S.count('#'))

    white = [0] * (N + 1)

    for i, s in enumerate(S, start=1):
        white[i] += white[i - 1]
        if s == '.':
            white[i] += 1

    for mid, s in enumerate(S):
        # 左をすべて白にする
        left = (mid - white[mid])

        # 右をすべて黒にする
        right = white[N] - white[mid + 1]

        ans = min(ans, left + right)

    print(ans)

sol()