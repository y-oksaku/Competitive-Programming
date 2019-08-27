import sys
import heapq
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10**9 + 7
INF = float('inf')

# MODにおける逆元
def modInv(a, MOD=1000000007) :
    b = MOD
    u = 1
    v = 0
    while b :
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u
    u = u % MOD
    return u

def sol():
    A = int(input())
    B = int(input())
    C = int(input())

    col = ((B * C - A * B) % MOD) * modInv(A * B + A * C - B * C) % MOD
    row = ((B * C - A * C) % MOD) * modInv(A * B + A * C - B * C) % MOD

    print(row, col)


sol()