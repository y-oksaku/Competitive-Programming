import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')
EPS = 1e-8

def sol():
    N = int(input())

    P = []

    for _ in range(N):
        x, y, c = map(int, input().split())
        P.append((x, y, c))

    # 左右で釣り合うxを探索
    # 右側が大きい/大きくない で二分探索
    def isOkX(cx):
        left = 0
        right = 0
        for x, _, c in P:
            if x <= cx:
                left = max(left, c * abs(x - cx))
            else:
                right = max(right, c * abs(x - cx))
        if right > left:
            return True
        return False

    ng = 10**5
    ok = -10**5

    while abs(ng - ok) > EPS:
        mid = (ng + ok) / 2
        if isOkX(mid):
            ok = mid
        else:
            ng = mid

    X = ok

    # 上下で釣り合うyを探索
    # 上が大きい/大きくない で二分探索
    def isOkY(cy):
        top = 0
        bottom = 0
        for _, y, c in P:
            if y <= cy:
                bottom = max(bottom, c * abs(cy - y))
            else:
                top = max(top, c * abs(cy - y))
        if top > bottom:
            return True
        return False

    ng = 10**5
    ok = -10**5

    while abs(ng - ok) > EPS:
        mid = (ng + ok) / 2
        if isOkY(mid):
            ok = mid
        else:
            ng = mid

    Y = ok

    ans = 0
    for x, y, c in P:
        ans = max(ans, c * max(abs(x - X), abs(y - Y)))

    print(ans)

sol()