from bisect import bisect_right, bisect_left

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i, a in enumerate(L):
    for j, b in enumerate(L[i + 1:], start=i + 1):
        left = bisect_right(L, abs(a - b))
        right = bisect_left(L, a + b)
        ans += right - left

        if left <= i < right:
            ans -= 1
        if left <= j < right:
            ans -= 1

print(ans // 3)
