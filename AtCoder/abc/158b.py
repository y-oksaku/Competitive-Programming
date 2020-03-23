N, A, B = map(int, input().split())
S = A + B

ans = (N // S) * A
ans += min(A, N % S)

print(ans)