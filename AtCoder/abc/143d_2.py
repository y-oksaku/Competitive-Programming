from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i, A in enumerate(L):
    for j, B in enumerate(L[i + 1:], start=i + 1):
        right = bisect_left(L, A + B)
        ans += right - j - 1

print(ans)