N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    if (X[i + 1] - X[i]) * A > B:
        ans += B
    else:
        ans += (X[i + 1] - X[i]) * A

print(ans)