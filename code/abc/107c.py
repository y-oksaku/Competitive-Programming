N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float('inf')

for left in range(N - K + 1) :
    if X[left] < 0 and X[left + K - 1] >= 0 :
        l = -X[left] * 2 + X[left + K - 1]
        r = -X[left] + X[left + K - 1] * 2
        ans = min(ans, l, r)
    elif X[left + K - 1] < 0 :
        ans = min(ans, -X[left])
    else :
        ans = min(ans, X[left + K - 1])

print(ans)