import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter, namedtuple
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

def sol():
    Ax, Ay, Bx, By = map(int, input().split())
    N = int(input())

    XY = namedtuple('XY', ('x', 'y'))

    A = XY(Ax, Ay)
    B = XY(Bx, By)

    points = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        points[i] = XY(x, y)

    points.append(points[0])

    def isCross(a, b, p, q):
        v = XY(a.y - b.y, -(a.x - b.x))

        crossP = (v.x * p.x + v.y * p.y) - (v.x * a.x + v.y * a.y)
        crossQ = (v.x * q.x + v.y * q.y) - (v.x * a.x + v.y * a.y)

        if crossP * crossQ < 0:
            return True
        return False

    count = 0
    for i in range(N):
        p = points[i]
        q = points[i + 1]

        if isCross(p, q, A, B) and isCross(A, B, p, q):
            count += 1

    print(count // 2 + 1)


sol()