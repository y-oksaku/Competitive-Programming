N, M = map(int, input().split())

tOne = M * 1900 + (N - M) * 100

ans = tOne * (2**M)
print(ans)