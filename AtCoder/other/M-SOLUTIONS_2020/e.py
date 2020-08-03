import sys
input = sys.stdin.buffer.readline
from numba import njit, prange
import numpy as np
INF = 10**18

@njit('(i8, i8[:,:])')
def solve(N, XYP):
    X = XYP[:, 0]
    Y = XYP[:, 1]

    def calcCost(sign, A):
        ret = np.ones((1 << N, N), dtype=np.int64) * INF
        for state in range(1 << N):
            useA = [a for i, a in enumerate(A) if (state & (1 << i)) != 0]
            for i in range(N):
                xyp = XYP[i]
                cost = abs(xyp[sign])
                for z in useA:
                    cost = min(cost, abs(xyp[sign] - z))
                ret[state][i] = cost * xyp[2]
        return ret

    costX = calcCost(0, X)
    costY = calcCost(1, Y)
    ans = np.ones(N + 1, dtype=np.int64) * INF

    for state in range(pow(3, N)):
        stateX = 0
        stateY = 0
        M = N
        for _ in range(N):
            state, r = divmod(state, 3)
            stateX <<= 1
            stateY <<= 1
            if r == 0: M -= 1
            if r == 1: stateX |= 1
            if r == 2: stateY |= 1

        cx, cy = costX[stateX], costY[stateY]
        cost = 0
        for i in range(N):
            cost += min(cx[i], cy[i])
        ans[M] = min(ans[M], cost)

    for a in ans:
        print(a)

def sol():
    N = int(input())
    XYP = np.asarray([list(map(int, input().split())) for _ in range(N)])
    solve(N, XYP)

sol()
