N, A, B = map(int, input().split())

dynamic = min(N, 5)

ans = N * A - (A - B) * dynamic
print(ans)