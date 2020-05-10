N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

X -= sum(M)
ans = N + X // min(M)
print(ans)
