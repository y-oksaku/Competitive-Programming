import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7

def diff(s):
    if s == 'a': return 0
    if s == 'b': return 25
    if s == 'c': return 24
    if s == 'd': return 23
    if s == 'e': return 22
    if s == 'f': return 21
    if s == 'g': return 20
    if s == 'h': return 19
    if s == 'i': return 18
    if s == 'j': return 17
    if s == 'k': return 16
    if s == 'l': return 15
    if s == 'm': return 14
    if s == 'n': return 13
    if s == 'o': return 12
    if s == 'p': return 11
    if s == 'q': return 10
    if s == 'r': return 9
    if s == 's': return 8
    if s == 't': return 7
    if s == 'u': return 6
    if s == 'v': return 5
    if s == 'w': return 4
    if s == 'x': return 3
    if s == 'y': return 2
    if s == 'z': return 1

def sol():
    S = list(input().strip())
    K = int(input())

    for i, s in enumerate(S):
        if s == 'a':
            continue
        else:
            if diff(s) <= K:
                S[i] = 'a'
                K -= diff(s)

    last = K % 26
    S[-1] = chr(ord(S[-1]) + last)
    print(*S, sep='')

sol()