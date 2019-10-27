import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from itertools import product
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def sol():
    K, N = map(int, input().split())

    words = []
    for _ in range(N):
        n, w = input().split()
        words.append([n, w])

    for numLeng in product([1, 2, 3], repeat=K):
        numToW = {}
        for num, word in words:
            now = 0
            for n in num:
                sub = word[now: numLeng[int(n) - 1] + now]
                now += numLeng[int(n) - 1]
                if n in numToW:
                    if sub != numToW[n]:
                        break
                else:
                    numToW[n] = sub
            else:
                if now < len(word):
                    break
                continue
            break
        else:
            for i in range(1, K + 1):
                print(numToW[str(i)])
            break



sol()