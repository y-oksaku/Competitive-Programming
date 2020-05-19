N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for left in range(N + 1):
    for right in range(N + 1):
        if left + right > N or left + right > K:
            continue
        L = V[:left]
        R = V[::-1][:right]

        A = L + R
        A.sort(reverse=True)
        k = K - (left + right)
        while k > 0 and A and A[-1] < 0:
            A.pop()
            k -= 1
        ans = max(ans, sum(A))
print(ans)
