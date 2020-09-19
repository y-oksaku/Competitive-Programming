import sys
import numpy as np

if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC
    cc = CC('my_module')

    @cc.export('solve', 'i4(i4, i4[:])')
    def solve(N, P):
        minDist = np.ones((N, N), dtype=np.int32)
        isFilled = np.ones((N, N), dtype=np.int32)

        for h in range(N):
            for w in range(N):
                minDist[h][w] = min(h, N - h - 1, w, N - w - 1)

        ans = 0
        for p in P:
            h, w = divmod(p, N)
            ans += minDist[h][w]
            isFilled[h][w] = False

            st = [(h, w)]
            while st:
                h, w = st.pop()
                dist = minDist[h][w] + isFilled[h][w]

                if h + 1 < N and minDist[h + 1][w] > dist:
                    minDist[h + 1][w] = dist
                    st.append((h + 1, w))
                if h - 1 >= 0 and minDist[h - 1][w] > dist:
                    minDist[h - 1][w] = dist
                    st.append((h - 1, w))
                if w + 1 < N and minDist[h][w + 1] > dist:
                    minDist[h][w + 1] = dist
                    st.append((h, w + 1))
                if w - 1 < N and minDist[h][w - 1] > dist:
                    minDist[h][w - 1] = dist
                    st.append((h, w - 1))
        return ans

    cc.compile()
    exit(0)

from my_module import solve

N = int(input())
P = np.asarray(list(map(lambda a: int(a) - 1, input().split())), dtype=np.int32)

print(solve(N, P))
