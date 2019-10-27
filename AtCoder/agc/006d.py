import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    H, W = map(int, input().split())
    chart = [0] * H

    for h in range(H):
        line = input().strip()
        chart[h] = line

    confilm = [[False] * W for _ in range(H)]

    def search(h, w):
        black = 0
        left, right = w, w
        confilm[h][w] = True

        st = deque([])
        st.append((h, w))

        while st:
            nH, nW = st.pop()

            black += 1

            for toH in range(nH - 1, nH + 2):
                for toW in range(nW - 1, nW + 2):
                    if chart[toH][toW] == 'o' and (not confilm[toH][toW]):
                        left = min(left, toW)
                        right = max(right, toW)
                        st.append((toH, toW))
                        confilm[toH][toW] = True
        return (black, (right - left + 1) // 5)

    A, B, C = 0, 0, 0
    for h in range(H):
        for w in range(W):
            if chart[h][w] == 'o':
                if not confilm[h][w]:
                    black, scale = search(h, w)
                    unit = black // (scale**2)
                    if unit == 12:
                        A += 1
                    elif unit == 16:
                        B += 1
                    else:
                        C += 1

            confilm[h][w] = True

    print(A, B, C)

sol()