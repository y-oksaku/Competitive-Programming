N = int(input())
A = list(map(int, input().split()))

ans = 1
right = 0
V = set()
for left in range(N):
    while right < N and not A[right] in V:
        V.add(A[right])
        right += 1
    ans = max(ans, right - left)
    V.remove(A[left])

print(ans)