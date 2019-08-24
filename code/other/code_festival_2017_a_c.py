import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def sol():
    H, W = map(int, input().split())
    chars = []

    for _ in range(H):
        chars += list(input().strip())

    cnt = Counter(chars)

    if H % 2 == 0 and W % 2 == 0:
        for _, c in cnt.items():
            if c % 4 != 0:
                print('No')
                return
        print('Yes')
        return
    elif H % 2 == 0 or W % 2 == 0:
        twoCount = 0
        if H % 2 == 0:
            twoCount = H // 2
        else:
            twoCount = W // 2
        for _, c in cnt.items():
            if c % 4 == 0:
                continue
            if c % 2 == 0:
                twoCount -= 1
            else:
                print('No')
                return
        if twoCount >= 0:
            print('Yes')
        else:
            print('No')
        return
    else:
        oneCount = 0
        twoCount = H // 2 + W // 2
        for _, c in cnt.items():
            if c % 4 == 1:
                oneCount += 1
                continue
            if c % 4 == 3:
                oneCount += 1
                twoCount -= 1
                continue
            if c % 4 == 0:
                continue
            if c % 2 == 0:
                twoCount -= 1
                continue
            print('No')
            return
        if oneCount == 1 and twoCount >= 0:
            print('Yes')
        else:
            print('No')


sol()