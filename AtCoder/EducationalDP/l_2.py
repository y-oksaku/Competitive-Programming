import sys
sys.setrecursionlimit(10 ** 7)
from functools import lru_cache

N = int(input())
A = list(map(int, input().split()))

@lru_cache(maxsize=None)
def seach(left, right, turn):
    if right - left == 1:
        if turn == 0:
            return A[left]
        else:
            return -A[left]

    if turn == 0:  # 最大化
        return max(seach(left + 1, right, 1) + A[left], seach(left, right - 1, 1) + A[right - 1])
    else:
        return min(seach(left + 1, right, 0) - A[left], seach(left, right - 1, 0) - A[right - 1])

ans = seach(0, N, 0)
print(ans)
