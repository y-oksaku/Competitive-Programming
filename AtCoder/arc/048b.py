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
    A = []
    gcp = [0, 0, 0]

    for i in range(N):
        r, h = map(int, input().split())
        h -= 1
        A.append((r, h, i))
        gcp[h] += 1

    A.sort(key=itemgetter(0))

    gcpSum = [[0] * 3 for _ in range(N + 1)]
    for i, (_, h, _)in enumerate(A):
        for j in range(3):
            gcpSum[i + 1][j] += gcpSum[i][j]
        gcpSum[i + 1][h] += 1


    ans = [0] * N
    for i, (r, h, index) in enumerate(A):
        right = bisect_right(A, (r, INF, INF))
        left = bisect_left(A, (r, -1, -1))
        win = left + (gcpSum[right][(h + 1) % 3] - gcpSum[left][(h + 1) % 3])
        lose = N - right + ((gcpSum[right][(h + 2) % 3] - gcpSum[left][(h + 2) % 3]))
        draw = (gcpSum[right][h % 3] - gcpSum[left][h % 3]) - 1

        ans[index] = (win, lose, draw)

    for w, l, d in ans:
        print(w, l, d)

sol()